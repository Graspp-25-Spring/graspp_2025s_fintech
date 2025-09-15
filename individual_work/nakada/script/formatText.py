import functionsNakada

# how to use "getTableFromPDF"
# you need to set two parameters getTableFromPDF(file, pages)
# file: "1" for CAMS report
# pages: [80,81,82] => pages you want to extract

# pages = [85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115]
# res = functionsNakada.getTableFromPDF(1, pages)

pages = [69, 110, 111,112,113,114]
res = functionsNakada.getTableFromPDF(2, pages)