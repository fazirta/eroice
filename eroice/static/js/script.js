function global() {
    return {
      isMobileMenuOpen: false,
      isDarkMode: false,
      themeInit() {
        if (
          localStorage.theme === "dark"
        ) {
          localStorage.theme = "dark";
          document.documentElement.classList.add("dark");
          this.isDarkMode = true;
        } else {
          localStorage.theme = "light";
          document.documentElement.classList.remove("dark");
          this.isDarkMode = false;
        }
      },
      themeSwitch() {
        if (localStorage.theme === "dark") {
          localStorage.theme = "light";
          document.documentElement.classList.remove("dark");
          this.isDarkMode = false;
        } else {
          localStorage.theme = "dark";
          document.documentElement.classList.add("dark");
          this.isDarkMode = true;
        }
      },
    };
  }