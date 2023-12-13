LOGIN_URL = 'https://www.capcut.com/login'
LOGIN_EMAIL = ""
LOGIN_PASSWORD = ""
DASHBOARD_URL = "https://www.capcut.com/editor?enter_from=create_new&from_page=work_space&__action_from=my_draft&position=my_draft&scenario=tiktok_ads&scale=9%3A16"
FILTER_TYPE_EXPAND_XPATH='//*[@id="expandable-tags__list-wrapper"]/div[3]/div'

# FILTER_DICT_WITH_EXPAND = {
#     'Life': '//*[@id="expandable-tags__list-wrapper"]/div[2]/div[5]',
#     'Food': '//*[@id="expandable-tags__list-wrapper"]/div[2]/div[6]',
#     'Movies': '//*[@id="expandable-tags__list-wrapper"]/div[2]/div[7]',
#     'Night Scene': '//*[@id="expandable-tags__list-wrapper"]/div[2]/div[8]',
#     'Scenery': '//*[@id="expandable-tags__list-wrapper"]/div[2]/div[9]',
#     'Retro': '//*[@id="expandable-tags__list-wrapper"]/div[2]/div[10]',
#     'Mono': '//*[@id="expandable-tags__list-wrapper"]/div[2]/div[11]',
#     'Style': '//*[@id="expandable-tags__list-wrapper"]/div[2]/div[12]',
# }

# FILTER_DICT_WITH_EXPAND = {
#     'Life': "//*[text()='Life']",
#     'Food': "//*[text()='Food']",
#     'Movies': "//*[text()='Movies']",
#     'Night Scene': "//*[text()='Night Scene']",
#     'Scenery': "//*[text()='Scenery']",
#     'Retro': "//*[text()='Retro']",
#     'Mono': "//*[text()='Mono']",
#     'Style': "//*[text()='Style']",
# }

# FILTER_DICT_WITHOUT_EXPAND = {
#     'Life': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]',
#     'Food': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]',
#     'Movies': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]',
#     'Night Scene': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[4]/div/div[2]/div[2]',
#     'Scenery': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[4]/div/div[2]/div[2]',
#     'Retro': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[4]/div/div[2]/div[2]',
#     'Mono': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[4]/div/div[2]/div[2]',
#     'Style': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[5]/div/div[2]/div[2]',
# }

FILTER_DICT_WITHOUT_EXPAND = {
    'Life': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]',
    'Food': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[4]/div/div[2]/div[2]',
    'Movies': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[5]/div/div[2]/div[2]',
    'Night Scene': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[4]/div/div[2]/div[2]',
    'Scenery': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]',
    'Retro': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[3]/div/div[2]/div[2]',
    'Mono': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[4]/div/div[2]/div[2]',
    'Style': '//*[@id="lv-tabs-2-panel-0"]/div/div/div[1]/div/div/div[5]/div/div[2]/div[2]',
}
FOR_1200_WIDTH_VIDEO_BAR=275

POPUP_XPATH = "/html/body/div[10]/div[4]/div/button"
BASIC_INTENSITY_XPATH = '//*[@id="attribute-panel-wrapper"]/div/div/div[3]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_COLOR_ADJUSTMENT_XPATH = '//*[@id="attribute-panel-wrapper"]/div/div/div[3]/div/div/div/div[3]'
BASIC_COLOR_ADJUSTMENT_COLOR_SATURATION_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_COLOR_ADJUSTMENT_COLOR_TEMPERATURE_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[3]/div[4]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_COLOR_ADJUSTMENT_LIGHTNESS_BRIGHTNESS_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[5]/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_COLOR_ADJUSTMENT_LIGHTNESS_CONTRAST_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[5]/div[4]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_COLOR_ADJUSTMENT_LIGHTNESS_SHINE_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[5]/div[6]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_COLOR_ADJUSTMENT_LIGHTNESS_HIGHLIGHT_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[5]/div[8]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_COLOR_ADJUSTMENT_LIGHTNESS_SHADOW_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[5]/div[10]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'

BASIC_BLEND_OPACITY_XPATH='//*[@id="attribute-panel-wrapper"]/div/div/div[3]/div/div/div/div[5]/div[3]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_TRANSFORM_SCALE_XPATH='//*[@id="attribute-panel-wrapper"]/div/div/div[3]/div/div/div/div[7]/div[2]/div[2]/div/div[1]/div/div/div/div/div[2]/div/span/span/input'
BASIC_TRANSFORM_POSITION_X_XPATH='//*[@id="attribute-panel-wrapper"]/div/div/div[3]/div/div/div/div[7]/div[3]/div[2]/div/div[1]/div/div[1]/div/span/span/input'
BASIC_TRANSFORM_POSITION_Y_XPATH='//*[@id="attribute-panel-wrapper"]/div/div/div[3]/div/div/div/div[7]/div[3]/div[2]/div/div[1]/div/div[2]/div/span/span/input'
BASIC_TRANSFORM_ROTATE_XPATH='//*[@id="attribute-panel-wrapper"]/div/div/div[3]/div/div/div/div[7]/div[4]/div[2]/div/div[1]/div/div[1]/div/span/span/input'
BASIC_EFFECT_SHARPNESS_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[7]/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_EFFECT_VIGNETTE_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[7]/div[4]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_EFFECT_FADE_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[7]/div[6]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'
BASIC_EFFECT_GRAIN_XPATH='//*[@id="lv-tabs-5-panel-0"]/div/div/div[7]/div[8]/div[2]/div/div[1]/div/div/div/div[2]/div/span/span/input'

SMART_TOOLS_XPATH='/html/body/div[8]/div/button[3]'
SMART_TOOLS_RETOUCH_XPATH='//*[@id="attribute-panel-wrapper"]/div/div/div[3]/div/div/div/div[2]'
SMART_TOOLS_RETOUCH_BODY_XPATH='//*[@id="attribute-panel-wrapper"]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[4]'

SMART_TOOLS_RETOUCH_BODY_SLIM_XPATH='//*[@id="lv-tabs-6-panel-3"]/div/div/div[2]/div/div[2]/div/div/div[2]/div/span/span/input'
SMART_TOOLS_RETOUCH_BODY_LEGS_XPATH='//*[@id="lv-tabs-6-panel-3"]/div/div/div[3]/div/div[2]/div/div/div[2]/div/span/span/input'
SMART_TOOLS_RETOUCH_BODY_WAIST_XPATH='//*[@id="lv-tabs-6-panel-3"]/div/div/div[4]/div/div[2]/div/div/div[2]/div/span/span/input'
SMART_TOOLS_RETOUCH_BODY_HEAD_XPATH='//*[@id="lv-tabs-6-panel-3"]/div/div/div[5]/div/div[2]/div/div/div[2]/div/span/span/input'
SMART_TOOLS_RETOUCH_BODY_SMOOTH_XPATH='//*[@id="lv-tabs-6-panel-3"]/div/div/div[6]/div/div[2]/div/div/div[2]/div/span/span/input'
SMART_TOOLS_RETOUCH_BODY_BRIGHTEN_XPATH='//*[@id="lv-tabs-6-panel-3"]/div/div/div[7]/div/div[2]/div/div/div[2]/div/span/span/input'

EXPORT_BUTTON='//*[@id="export-video-btn"]'
DOWNLOAD_BUTTON='/html/body/div[9]/span/div[1]/div/div[4]/button'
CONFIRM_EXPORT_BUTTON='//*[@id="export-confirm-button"]'
CONFIRM_DOWNLOAD_BUTTON='/html/body/div[10]/div[2]/div/div/div[2]/div[1]/div/div[2]/button'
x='lv-btn lv-btn-secondary lv-btn-size-default lv-btn-shape-square downloadButton'