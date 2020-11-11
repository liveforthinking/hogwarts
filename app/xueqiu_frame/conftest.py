def exception_handle(fun):
    def swapper(*args, **kwargs):
        from app.xueqiu_frame.page.base_page import BasePage
        instance: BasePage = args[0]
        try:
            result = fun(*args, **kwargs)
            instance._error_count = 0
            return result
        except Exception as e:
            instance._error_count += 1
            if instance._error_count > instance._error_max:
                raise e
            instance.driver.implicitly_wait(0)
            for element in instance._black_list:
                elements = instance.driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    instance.driver.implicitly_wait(10)
                    return fun(*args, **kwargs)

    return swapper
