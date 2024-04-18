class BookmarkManager:
    def __init__(self):
        self.bookmarks = []

    def add_bookmark(self, title, url):
        new_bookmark = {"title": title, "url": url}
        self.bookmarks.append(new_bookmark)
        print(f"Добавлена новая закладка: {title}")

    def remove_bookmark(self, index):
        if 0 <= index < len(self.bookmarks):
            removed_bookmark = self.bookmarks.pop(index)
            print(f"Удалена закладка: {removed_bookmark['title']}")
        else:
            print("Ошибка: неверный индекс закладки")

    def list_bookmarks(self):
        print("Список закладок:")
        for index, bookmark in enumerate(self.bookmarks, 1):
            print(f"{index}. {bookmark['title']} - {bookmark['url']}")


# Пример использования:
bookmark_manager = BookmarkManager()
bookmark_manager.add_bookmark("Google", "https://www.google.com")
bookmark_manager.add_bookmark("Facebook", "https://www.facebook.com")
bookmark_manager.add_bookmark("Twitter", "https://twitter.com")
bookmark_manager.list_bookmarks()
bookmark_manager.remove_bookmark(1)
bookmark_manager.list_bookmarks()