import qpy
import androidhelper
import urllib.request as ur
from qsl4ahelper.fullscreenwrapper2 import *
from IP import *
from Host import *
from Connect import *
droid = androidhelper.Android()

class MainScreen(Layout):
    def __init__(self):
        super(MainScreen,self).__init__(str("""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
	android:layout_width="fill_parent"
	android:layout_height="fill_parent"
	android:background="#000000"
	android:orientation="vertical"
	xmlns:android="http://schemas.android.com/apk/res/android">

	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:orientation="horizontal"
		android:layout_weight="20">

		<TextView
			android:layout_width="fill_parent"
			android:layout_height="fill_parent"
			android:textSize="8dp"
			android:text="Server App"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"
		/>
    </LinearLayout>

	<ListView
		android:id="@+id/data_list"
		android:layout_width="fill_parent"
		android:layout_height="0px"
		android:layout_weight="55"/>

	<LinearLayout
		android:layout_width="fill_parent"
		android:layout_height="1000px"
		android:orientation="horizontal"
		android:layout_weight="8">
		<Button
			android:layout_width="fill_parent"
			android:layout_height="wrap_content"
			android:text="Get own IP"
			android:id="@+id/but_getip"
			android:textSize="8dp"
			android:background="#808080"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"
			android:layout_gravity="bottom"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="wrap_content"
			android:text="Host"
			android:id="@+id/but_host"
			android:textSize="8dp"
			android:background="#808080"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"
			android:layout_gravity="bottom"/>
		<Button
			android:layout_width="fill_parent"
			android:layout_height="wrap_content"
			android:text="Exit"
			android:id="@+id/but_exit"
			android:textSize="8dp"
			android:background="#808080"
			android:textColor="#ffffffff"
			android:layout_weight="1"
			android:gravity="center"
			android:layout_gravity="bottom"/>
	</LinearLayout>
</LinearLayout>
"""),"SL4AApp")

    def on_show(self):
        self.views.but_exit.add_event(click_EventHandler(self.views.but_exit, self.exit))
        self.views.but_getip.add_event(click_EventHandler(self.views.but_getip, self.get_ip))
        self.views.but_host.add_event(click_EventHandler(self.views.but_host, self.host))
        pass

    def on_close(self):
        pass

    def get_ip(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        find_ip()
        droid.makeToast("IP logged")

    def exit(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        FullScreenWrapper2App.close_layout()

    def host(self, view, dummy):
        droid = FullScreenWrapper2App.get_android_instance()
        host()
        droid.makeToast("Hosting...")
        
if __name__ == '__main__':
    FullScreenWrapper2App.initialize(droid)
    FullScreenWrapper2App.show_layout(MainScreen())
    FullScreenWrapper2App.eventloop()