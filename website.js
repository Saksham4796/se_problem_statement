window.onload = function() {
  // Get the HTML table element
  const table = document.querySelector('table');

  // Add "zebra-striping" to the table rows
  const rows = table.querySelectorAll('tr:not(:first-child)');
  for (let i = 0; i < rows.length; i++) {
    if (i % 2 == 0) {
      rows[i].style.backgroundColor = '#f9f9f9';
    } else {
      rows[i].style.backgroundColor = '#fff';
    }
  }

  // Make the table sortable
  const headers = table.querySelectorAll('th');
  for (let i = 0; i < headers.length; i++) {
    headers[i].addEventListener('click', function() {
      const column = this.dataset.column;
      const order = this.dataset.order;
      const rows = table.querySelectorAll('tbody tr');
      const sortedRows = Array.from(rows).sort(function(a, b) {
        const aVal = a.querySelector('td:nth-child(' + (parseInt(column) + 1) + ')').textContent.trim();
        const bVal = b.querySelector('td:nth-child(' + (parseInt(column) + 1) + ')').textContent.trim();
        if (isNaN(aVal) || isNaN(bVal)) {
          return aVal.localeCompare(bVal, undefined, {numeric: true, sensitivity: 'base'});
        } else {
          return parseFloat(aVal) - parseFloat(bVal);
        }
      });
      if (order == 'desc') {
        sortedRows.reverse();
        this.dataset.order = 'asc';
      } else {
        this.dataset.order = 'desc';
      }
      for (let i = 0; i < rows.length; i++) {
        rows[i].parentNode.removeChild(rows[i]);
      }
      for (let i = 0; i < sortedRows.length; i++) {
        table.querySelector('tbody').appendChild(sortedRows[i]);
      }
    });
  }
};

