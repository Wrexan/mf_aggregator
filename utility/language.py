import json
from dataclasses import dataclass


@dataclass
class Language:
    def __init__(self, config):
        self.C = config
        self.apply_as_attrs = 'main'
        self.load_language()

    def load_language(self):
        with open(f'{self.C.LANG_PATH}\\{self.C.LANGS[self.C.CURRENT_LANG]}', 'r', encoding='utf-8') as f:
            lang_data = json.load(f)
        for module_name, module_attrs in lang_data.items():
            if module_name == self.apply_as_attrs:
                for text_elem in lang_data[module_name].items():
                    self.__setattr__(*text_elem)
            else:
                self.__setattr__(module_name, lang_data[module_name])

    def apply_lang_to_all_app(self):
        ...

    def translate_config_texts(self, module):
        for i in self.config['PRICE_STATUSES']:
            module.PRICE_STATUSES[i] = self.config['PRICE_STATUSES'][i]
        module.DK9_TABLE_NAMES = (*self.config['DK9_TABLE_NAMES'],)
        for i in self.config['WEB_STATUSES']:
            module.WEB_STATUSES[i] = self.config['WEB_STATUSES'][i]

    def translate_MainWindow_texts(self, module):
        module.help.setText(self.MainWindow["help"])
        module.settings_button.setText(self.MainWindow["settings_button"])
        module.graph_button.setText(self.MainWindow["graph_button"])
        module.chb_show_exact.setText(self.MainWindow["chb_show_exact"])
        module.chb_show_date.setText(self.MainWindow["chb_show_date"])
        module.pb_adv_search.setText(self.MainWindow["pb_adv_search"])
        module.chb_price_name_only.setText(self.MainWindow["chb_price_name_only"])
        module.chb_search_eng.setText(self.MainWindow["chb_search_eng"])
        module.chb_search_narrow.setText(self.MainWindow["chb_search_narrow"])

    def translate_AdvSearchDialog_texts(self, module):
        module.setWindowTitle(self.AdvSearchDialog["WindowTitle"])
        module.ui.label_2.setText(self.AdvSearchDialog["label_2"])
        module.ui.label.setText(self.AdvSearchDialog["label"])
        module.ui.label_3.setText(self.AdvSearchDialog["label_3"])
        module.ui.label_4.setText(self.AdvSearchDialog["label_4"])
        module.ui.label_5.setText(self.AdvSearchDialog["label_5"])

    def translate_StartWindow_texts(self, module):
        module.setWindowTitle(self.StartWindow["WindowTitle"])
        module.ui.label_6.setText(self.StartWindow["label_6"])
        module.ui.label_5.setText(self.StartWindow["label_5"])
        module.ui.frame_11.setToolTip(self.StartWindow["frame_11_ToolTip"])
        # module.ui.frame_11.setStatusTip(self.StartWindow["start_window", "2"])
        # module.ui.frame_11.setWhatsThis(self.StartWindow["start_window", "1"])
        module.ui.label_7.setText(self.StartWindow["label_7"])
        module.ui.label_8.setText(self.StartWindow["label_8"])
        module.ui.label.setText(self.StartWindow["label"])
        module.ui.label_2.setText(self.StartWindow["label_2"])
        module.ui.pb_stat_0.setText(self.StartWindow["pb_stat_0"])
        module.ui.label_3.setText(self.StartWindow["label_3"])
        module.ui.label_4.setText(self.StartWindow["label_4"])
        module.ui.pb_stat_1.setText(self.StartWindow["pb_stat_1"])
        module.ui.pb_stat_2.setText(self.StartWindow["pb_stat_2"])
        module.ui.pb_stat_3.setText(self.StartWindow["pb_stat_3"])

    def translate_ConfigWindow_texts(self, module):
        module.setWindowTitle(self.ConfigWindow["WindowTitle"])
        module.ui.label_6.setText(self.ConfigWindow["label_6"])
        module.ui.frame.setToolTip(self.ConfigWindow["frame_ToolTip"])
        module.ui.label_2.setText(self.ConfigWindow["label_2"])
        module.ui.label_3.setText(self.ConfigWindow["label_3"])
        module.ui.label_14.setText(self.ConfigWindow["label_14"])
        module.ui.frame_7.setToolTip(self.ConfigWindow["frame_7_ToolTip"])
        module.ui.label_9.setText(self.ConfigWindow["label_9"])
        module.ui.label_7.setText(self.ConfigWindow["label_7"])
        module.ui.lb_language.setText(self.ConfigWindow["lb_language"])
        module.ui.chk_fullscreen.setText(self.ConfigWindow["chk_fullscreen"])
        module.ui.label_11.setText(self.ConfigWindow["label_11"])
        module.ui.chb_show_exact.setText(self.ConfigWindow["chb_show_exact"])
        module.ui.chb_price_name_only.setText(self.ConfigWindow["chb_price_name_only"])
        module.ui.chb_search_eng.setText(self.ConfigWindow["chb_search_eng"])
        module.ui.chb_search_narrow.setText(self.ConfigWindow["chb_search_narrow"])
        module.ui.label_10.setText(self.ConfigWindow["label_10"])
        module.ui.label_4.setText(self.ConfigWindow["label_4"])
        module.ui.colored_price_table.setText(self.ConfigWindow["colored_price_table"])
        module.ui.word_wrap_web_table.setText(self.ConfigWindow["word_wrap_web_table"])
        module.ui.word_wrap_price_table.setText(self.ConfigWindow["word_wrap_price_table"])
        module.ui.colored_web_table.setText(self.ConfigWindow["colored_web_table"])
        module.ui.label_5.setText(self.ConfigWindow["label_5"])
        module.ui.label_8.setText(self.ConfigWindow["label_8"])
        module.ui.label_12.setText(self.ConfigWindow["label_12"])

