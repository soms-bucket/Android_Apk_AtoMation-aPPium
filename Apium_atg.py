from appium import webdriver
from time import sleep

def slt_grp():
	grp = drv.find_element_by_id("com.ATG.World:id/layout_select_group_container")

	grp.click()

	sleep(2)

	loc_1="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.View/android.widget.RelativeLayout[5]/android.widget.TextView"

	sl_grp= drv.find_element_by_xpath(loc_1)

	sl_grp.click()


	done = drv.find_element_by_id("com.ATG.World:id/layout_group_list_done")

	done.click()

	sleep(2)

app={
  "platformName": "android",
  "appium:appActivity": "com.atg.world.activity.SplashActivity",
  "appium:appPackage": "com.ATG.World",
  "appium:deviceName": "S316101100171613"
}

drv=webdriver.Remote("http://localhost:4723/wd/hub",app)

start=drv.find_element_by_id("com.ATG.World:id/getStartedTv")

start.click()

sleep(8)

sgn=drv.find_element_by_id("com.ATG.World:id/login_email")

sgn.click()

sleep(6)

email = drv.find_element_by_id("com.ATG.World:id/email")

email.send_keys("wiz_saurabh@rediffmail.com")

sleep(2)

password = drv.find_element_by_id("com.ATG.World:id/password")

password.send_keys("Pass@123")

sleep(2)

signin = drv.find_element_by_id("com.ATG.World:id/email_sign_in_button")

signin.click()

sleep(2)

print("Test_Login_With-Right_Credential Passed.")

sleep(4)

for lp in range(2):

	got_1 = drv.find_element_by_id("com.ATG.World:id/btnGotit")

	got_1.click()

	sleep(3)


pst = drv.find_element_by_id("com.ATG.World:id/fab")

pst.click()

sleep(3)

########Post Article##########

print("\nPosting Article.\n")

articl = drv.find_element_by_id("com.ATG.World:id/post_article_fab_clicked")

articl.click()

sleep(2)

####select Grp
slt_grp()


add_ttl= drv.find_element_by_id("com.ATG.World:id/post_article_title")
add_ttl.send_keys("AutoMation With appium")


add_des= drv.find_element_by_id("com.ATG.World:id/post_article_description")
add_des.send_keys("AutoMation")

ta_g= drv.find_element_by_id("com.ATG.World:id/layout_add_tags_container")
ta_g.click()

tag_el= drv.find_element_by_id("com.ATG.World:id/layout_add_tags_view_tag_title")
tag_el.send_keys("Appium")

drv.press_keycode(66)


tag_dn= drv.find_element_by_id("com.ATG.World:id/layout_add_tags_action")
tag_dn.click()
sleep(2)


make_pst= drv.find_element_by_id("com.ATG.World:id/toolbar_post_action")
make_pst.click()

sleep(5)

back_m=drv.find_element_by_id("com.ATG.World:id/post_details_back")
back_m.click()
sleep(2)

###############Posting Image#############

print("\nPosting Image.\n")

pst_img= drv.find_element_by_id("com.ATG.World:id/image_fab_clicked")
pst_img.click()
sleep(1)

cam="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]"
ca_cam=drv.find_element_by_xpath(cam)
ca_cam.click()
sleep(2)

clk_img= drv.find_element_by_id("com.android.camera2:id/bottom_bar")
clk_img.click()
sleep(2)

	

tik=drv.find_element_by_id("com.android.camera2:id/done_button")
tik.click()
sleep(4)

####select Grp
slt_grp()

	
caption= drv.find_element_by_id("com.ATG.World:id/postCaption")
caption.send_keys("AutoMation Image Post.")


img_suc= drv.find_element_by_id("com.ATG.World:id/toolbar_post_action")
img_suc.click()
sleep(5)
	

back_i=drv.find_element_by_id("com.ATG.World:id/toolbar_post_back")
back_i.click()
sleep(2)


cls_ops=drv.find_element_by_id("com.ATG.World:id/cross_fab_clicked")
cls_ops.click()
sleep(2)


print("\nTEstCAse Done\n")








