window.onload = () => {
  // run Carousel
  if (typeof(Carousel) != 'undefined') {
    window.carousel = new Carousel('carousel', {dataId: 1, isAutoSwitch: true})
    carousel.createCarousel() 
  }
  
  // header drop down trigger
  let headerDropdownTrigger = document.getElementById('header-user-name')
  if (headerDropdownTrigger) {
    headerDropdownTrigger.addEventListener('click', () => {
      let headerContainer = document.getElementById('header-dropdown-container')
      let headerDropDown  = document.getElementById('header-dropdown')
      headerContainer.style = 'display: block'
      headerDropDown.style = 'display: block'
    })
  }
}
