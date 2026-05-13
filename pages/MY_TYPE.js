const MY_TYPE = "의류"; // 농산물, 수산물, 의류, 기타

function getPortfolioTheme() {
  if (MY_TYPE === "농산물") {
    return "farm";
  }

  if (MY_TYPE === "수산물") {
    return "sea";
  }

  if (MY_TYPE === "의류") {
    return "fashion";
  }

  return "etc";
}

function applyPortfolioTheme() {
  document.body.dataset.theme = getPortfolioTheme();
}
