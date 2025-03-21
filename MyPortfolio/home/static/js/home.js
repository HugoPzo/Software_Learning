const codeElement = document.querySelector('.code');
    const text = codeElement.innerHTML;

    // Regular expression to match strings in the format 'text'
    const modifiedText = text.replace(/'([^']+)'/g, (match, p1) => `<span class="string">'${p1}'</span>`);

    // Apply the modified HTML to the element
    codeElement.innerHTML = modifiedText;

let index = 0;
        function moveSlide(step) {
            const slides = document.querySelectorAll('.carousel img');
            index = (index + step + slides.length) % slides.length;
            document.querySelector('.carousel').style.transform = `translateX(-${index * 100}%)`;
        }
