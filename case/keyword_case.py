#coding=utf-8

import sys
sys.path.append('F:\\Python\\5itest_po_3')

from util.excel_util import ExcelUtil
from keyword_selenium.actionMethod import ActionMethod

class KeywordCase():
    def run_main(self):
        self.action_method = ActionMethod('firefox')
        handle_excel = ExcelUtil('F:/Python/5itest_po_3/config/keywords-1.xls')
        case_lines = handle_excel.get_lines()
        for i in range(1,case_lines):
            is_run = handle_excel.get_value(i,3)
            if is_run == 'yes':
                method = handle_excel.get_value(i,4)
                send_value = handle_excel.get_value(i, 5)
                get_element = handle_excel.get_value(i, 6)
                except_result_method = handle_excel.get_value(i, 7)
                except_result = handle_excel.get_value(i, 8)
                self.run_method(method,get_element,send_value)
                if except_result:
                    except_value = self.get_except_result_value(except_result)
                    if except_value[0] == 'text':
                        result = self.run_method(except_result_method)
                        if except_value[1] in result:
                            handle_excel.write_value(i,'pass')
                        else:
                            handle_excel.write_value(i, 'fail')
                    elif except_value[0] == 'element':
                        result = self.run_method(except_result_method,except_value[1])
                        if result:
                            handle_excel.write_value(i, 'pass')
                        else:
                            handle_excel.write_value(i, 'fail')
            else:
                pass

        #拿到行数
        #循环行数，去执行每一行的case
        #是否执行
            #拿到执行方法
            #拿到操作元素
            #拿到输入的数据
            #是否有输入数据
                #执行方法（输入数据，操作元素）
            #没有输入数据
                #执行方法（操作元素）

    def get_except_result_value(self,data):
        result = data.split('=')
        return result

    def run_method(self,method,get_element='',send_value=''):
        run_method = getattr(self.action_method,method)
        if get_element != '' and send_value == '':
            result = run_method(get_element)  #open_browser,get_url,get_element
        elif get_element == '' and send_value != '':
            result = run_method(get_element)  #无此情况
        elif get_element != '' and send_value != '':
            result = run_method(get_element,send_value)  #element_send_key
        else:
            result = run_method()  #sleep_time,close_browser,get_title(预期结果)
        return result


if __name__ == '__main__':
    keyword_case = KeywordCase()
    keyword_case.run_main()