import gtk
import time

from foobnix.regui.notetab import NoteTabControl
from foobnix.regui.base_layout import BaseFoobnixLayout
from foobnix.regui.base_controls import BaseFoobnixControls
from foobnix.regui.treeview.musictree import MusicTreeControl
from foobnix.regui.window import MainWindow
from foobnix.regui.controls.filter import FilterControl
from foobnix.regui.controls.playback import PlaybackControls
import gobject
from foobnix.regui.search import SearchControls
from foobnix.regui.controls.seach_progress import SearchProgressBar
from foobnix.regui.infopanel import InfoPanelWidget
from foobnix.regui.engine.gstreamer import GStreamerEngine
from foobnix.regui.controls.seekbar import SeekProgressBarControls
from foobnix.regui.controls.volume import VolumeControls
from foobnix.regui.controls.status_bar import StatusbarControls
from foobnix.regui.treeview.radiotree import RadioTreeControl
from foobnix.regui.treeview.virtualtree import VirtualTreeControl
from foobnix.regui.controls.tray_icon import TrayIconControls
from foobnix.preferences.preferences_window import PreferencesWindow
class FoobnixCore(BaseFoobnixControls):
    
    def __init__(self):       
        BaseFoobnixControls.__init__(self)

        """elements"""
        
        self.preferences = PreferencesWindow(self)
        self.statusbar = StatusbarControls(self)
        self.volume = VolumeControls(self)
        self.seek_bar = SeekProgressBarControls(self)
        
        self.media_engine = GStreamerEngine(self)
        self.search_progress = SearchProgressBar(self)
        
        self.info_panel = InfoPanelWidget(self)
        
        self.searchPanel = SearchControls(self)   
        self.playback = PlaybackControls(self)     
        self.main_window = MainWindow(self)
        self.notetabs = NoteTabControl(self)
          
        self.filter = FilterControl(self)
        
        self.tree = MusicTreeControl(self)
        self.radio = RadioTreeControl(self)
        self.virtual = VirtualTreeControl(self)
        
        self.trayicon = TrayIconControls(self)
        self.trayicon.show()
               
        
        """layout"""        
        self.layout = BaseFoobnixLayout(self)
        
        self.on_load()
        
init_time = time.time()
gobject.threads_init()
#gtk.gdk.threads_enter()
eq = FoobnixCore()
print "******Foobnix run in", time.time() - init_time, " seconds******"
gtk.main()
    
