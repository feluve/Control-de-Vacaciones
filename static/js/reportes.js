// import XLSX from 'xlsx';

window.addEventListener("load", (event) => {
    console.log("Reportes");

});

function exportToExcel() {

    console.log("Exportar a Excel");

    // Obtener la tabla HTML
    var htmlTable = document.getElementById("miTabla");
  
    // Crear un objeto de libro de Excel
    var workbook = XLSX.utils.book_new();
  
    // Crear una hoja de cálculo y agregarla al libro de Excel
    var worksheet = XLSX.utils.table_to_sheet(htmlTable);
    XLSX.utils.book_append_sheet(workbook, worksheet, "Hoja1");
  
    // Descargar el archivo Excel
    XLSX.writeFile(workbook, "Reporte.xlsx");
  }