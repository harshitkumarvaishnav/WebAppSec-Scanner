def get_modules(testing_type: str):

    testing_type = testing_type.lower()

    if testing_type == "white_box":
        return [
            "url_validation",
            "dns",
            "http",
            "ssl",
            "headers",
            "robots"
        ]

    elif testing_type == "grey_box":
        return [
            "url_validation",
            "dns",
            "http",
            "ssl",
            "headers",
            "robots"
        ]

    elif testing_type == "black_box":
        return [
            "url_validation",
            "dns",
            "http",
            "ssl",
            "headers",
            "robots"
        ]

    elif testing_type == "red_team":
        return [
            "url_validation",
            "dns",
            "http",
            "ssl",
            "headers",
            "robots"
        ]

    return []