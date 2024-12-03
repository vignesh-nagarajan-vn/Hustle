function filterByCategory(filterValue) {
    const resultContainers = document.querySelectorAll('.result-container');
    resultContainers.forEach(container => {
        const categories = Array.from(container.querySelectorAll('.categories span'))
            .map(span => span.textContent.toLowerCase());
        const isMatch = categories.some(category => category.includes(filterValue.toLowerCase()));
        container.style.display = isMatch ? 'block' : 'none';
    });
}

function resetFilters() {
    const resultContainers = document.querySelectorAll('.result-container');
    resultContainers.forEach(container => {
        container.style.display = 'block';
    });
}

function performSearch() {
    const searchInput = document.getElementById('search-input');
    const query = searchInput.value.toLowerCase();
    const resultContainers = document.querySelectorAll('.result-container');
    const clearButton = document.getElementById('clear-button');
    clearButton.style.display = query ? 'inline' : 'none';

    resultContainers.forEach(container => {
        const title = container.querySelector('h4').textContent.toLowerCase();
        const description = container.querySelector('p').textContent.toLowerCase();
        const categories = Array.from(container.querySelectorAll('.categories span'))
            .map(span => span.textContent.toLowerCase())
            .join(" ");
        container.style.display = title.includes(query) || description.includes(query) || categories.includes(query) ? 'block' : 'none';
    });
}

function clearSearch() {
    const searchInput = document.getElementById('search-input');
    searchInput.value = '';
    performSearch();
}
