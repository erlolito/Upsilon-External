#include "extapp_api.h"
#include "img.h"

void extapp_main(void) {
    while(extapp_scanKeyboard())extapp_msleep(10);
    extapp_pushRectUniform(0,0,320,240,0xffff);
    for(unsigned int len=0;len<img_len;len++)extapp_pushRectUniform(len%320,len/320,1,1,img[len]);
    int key=extapp_getKey(true,NULL);
    if(key==KEY_CTRL_EXIT||key==KEY_CTRL_MENU)return;
}
