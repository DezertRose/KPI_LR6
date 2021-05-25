from AppsPage import SearchHelper

def test_search(browser):
    main_page = SearchHelper(browser)
    main_page.go.to.site()
    assert main_page.title == "Google Play"
    main_page.enter_words_input("Duskwood - Crime & Investigation Detective Story")
    main_page.click_on(1)
    main_page.click_on(2)
    assert main_page.current_url == "https://play.google.com/store/apps/details?id=com.everbytestudio.interactive.text.chat.story.rpg.cyoa.duskwood"
    el =  main_page.check_header()
    assert el == "Duskwood - Crime & Investigation Detective Story"

