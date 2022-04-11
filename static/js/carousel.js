window.onload = () => {
  // generate styles
  generateStylings()
  
  // get carousel container
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
  // carousel event listeners
  function carouselDotEventListener(){
    console.log(this.id)
    carouselPagesSwitcher(this.id)
  }
  
  // generate elements
  let carouselDotsContainer = document.createElement('div')
  carouselDotsContainer.classList.add('carousel-dots-container')
  Array.from(carouselItems).forEach(element => {
    let carouselDot = document.createElement('div')
    carouselDot.classList.add('carousel-dots')
    carouselDot.id = element.dataset.id
    carouselDot.addEventListener('click', carouselDotEventListener)
    carouselDotsContainer.appendChild(carouselDot)
  })
  
  carouselContainer.appendChild(carouselDotsContainer)
}

/**
 * Switch the pages of carousel by data id
 * @param {*} dataId 
 */
function carouselPagesSwitcher(dataId) {
  // remove active class
  let carouselDots = document.getElementsByClassName('carousel-dots')
  let carouselItems = document.getElementsByClassName('carousel-item')
  Array.from(carouselDots).forEach(el => {
    el.style = 'background-color: transparent'
    el.classList.remove('active-carousel-dot')
  })
  
  Array.from(carouselItems).forEach(el => {
    el.style = 'display: none'
  })
  
  // add active class to the element selected
  document.getElementById(`${dataId}`).classList.add('active-carousel-dot')
  Array.from(carouselItems).find(el => el.dataset.id == dataId).style = 'display: block'
}

function generatePerviousNextButtons(carouselContainer) {
  let leftButton = document.createElement('button')
  let rightButton = document.createElement('button')
  
}

/**
 * Generate css styles for the built in elements
 */
function generateStylings() {
  // generate styles
  let carouselDotStyles = document.createElement('style')
  let head = document.querySelector('head')
  carouselDotStyles.innerHTML = 
  `
  .carousel-item {
    animation: fade-in ease 1s 1;
  }
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
  .carousel-dots-container div:first-child {
    background-color: white;
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
    background-color: white !important;
  }
  @keyframes fade-in {
    0%    { opacity: .1; }
    100%   { opacity: 1; }
  }
  `
  
  head.appendChild(carouselDotStyles)  
}
