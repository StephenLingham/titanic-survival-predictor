<script>
    import { flip } from 'svelte/animate';

    let imageWidth = 500;
    let imageSpacing = '25px'; 
    let transitionSpeed = 500; 

    let images = [
        {path: '/Female_Male_survival_chance.png', id: 'image1', alt:'Female Male Survival Chance Graph'},
        {path: '/Ticket Class survival chance.png', id: 'image2', alt:'Ticket Class Survival Chance Graph'},
        {path: '/Survivability_age_histogram.png', id: 'image3', alt:'Survivability Age Histogram'}
    ]

    const rotateLeft = () => {
        const transitioningImage = images[images.length - 1];
        document.getElementById(transitioningImage.id).style.opacity = '0';
        images = [images[images.length -1],...images.slice(0, images.length - 1)];
        setTimeout(() => {document.getElementById(transitioningImage.id).style.opacity = '1'}, transitionSpeed);
    }

    const rotateRight = () => {
        const transitioningImage = images[0];
        document.getElementById(transitioningImage.id).style.opacity = '0';
        images = [...images.slice(1, images.length), images[0]];
        setTimeout(() => {document.getElementById(transitioningImage.id).style.opacity = '1'}, transitionSpeed);
    }
</script>

<div class="carousel-container">
    <div class="carousel-images">
    {#each images as image (image.id)}
      <img
        src={image.path}
        alt={image.alt}
        id={image.id}
        style={`width: ${imageWidth}px; margin: 0 ${imageSpacing}; border-radius: 25px`}
        animate:flip={{duration: transitionSpeed}}
      />
    {/each}
    </div>    
  </div>

  <button class="prev" on:click={rotateLeft}>Left</button>
  <button class="next" on:click={rotateRight}>Right</button>

  <style>
    .carousel-container {
        width: 100%;
        position: relative;
        display: flex;
        flex-direction: column;
        overflow-x: hidden;
    }
    .carousel-images {
        display: flex;
        justify-content: center;
        flex-wrap: nowrap;
    }
  </style>
