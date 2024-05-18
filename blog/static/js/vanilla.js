// Slider Carousel

var galleryTop = new Swiper(".detail-carousel", {
  spaceBetween: 10,
  loop: true,
  loopedSlides: 5, //looped slides should be the same
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  observer: true,
  observeParents: true,
  observeSlideChildren: true,
});
