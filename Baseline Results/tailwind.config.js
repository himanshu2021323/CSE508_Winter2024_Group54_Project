/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}", "./!(build|dist|.*)/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        gray: "#1f2833",
        aqua: "#66fcf1",
        white: "#fff",
        silver: "#b9b9b9",
        dodgerblue: "#0084fd",
        cadetblue: "#45a29e",
      },
      spacing: {},
      fontFamily: {
        inter: "Inter",
      },
      borderRadius: {
        "11xl": "30px",
      },
    },
    fontSize: {
      xl: "20px",
      "5xl": "24px",
      inherit: "inherit",
    },
  },
  corePlugins: {
    preflight: false,
  },
};
