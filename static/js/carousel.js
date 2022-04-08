window.onload = () => {
  let carouselContainer = document.getElementById('carousel')
  
  if(validateCarouselContainer(carouselContainer)) {
    let carouselItems = document.getElementsByClassName('carousel-item')
    generateRedirectionDots(carouselContainer, carouselItems)
  }
}

/**
 * validate carousel container
 * @param {*} carouselContainer 
 */
function validateCarouselContainer(carouselContainer) {
  let isValid = true
  if (!carouselContainer) {
    console.error('Can\'t find div element with id \'carousel\'')
    isValid = false
  }
  return isValid
}

/**
 * Generate redirection dots
 * @param {*} carouselContainer 
 * @param {*} carouselItems 
 */
function generateRedirectionDots(carouselContainer, carouselItems) {
  // generate styles
  let carouselDotStyles = document.createElement('style')
  let head = document.querySelector('head')
  carouselDotStyles.innerHTML = 
  `
  .carousel {
    position: relative;
  }
  .carousel-dots-container {
    position: absolute;
    z-index: 3;
    width: 100%;
    height: 23px;
    bottom: 23px;
    text-align: center;
  }
  .carousel-dots {
    padding: 5px;
    border-radius: 30px;
    display: inline-block;
    margin: 0px 5px;
    border: solid 1px white;
    cursor: pointer;
  }
  .carousel-dots:hover {
    background-color: white;
  }
  .active-carousel-dot {
    background-color: white;
  }
  `
  
  head.appendChild(carouselDotStyles)
  
  // carousel event listeners
  function carouselDotEventListener(){
    console.log(carouselItems)
  }
  
  // generate elements
  let carouselDotsContainer = document.createElement('div')
  carouselDotsContainer.classList.add('carousel-dots-container')
  Array.from(carouselItems).forEach(element => {
    let carouselDot = document.createElement('div')
    carouselDot.classList.add('carousel-dots')
    carouselDot.addEventListener('click', carouselDotEventListener)
    carouselDotsContainer.appendChild(carouselDot)
  })
  
  carouselContainer.appendChild(carouselDotsContainer)
}
