<script>
    // We import our page components (similar to the one above).
    import P1Gender from './P1Gender.svelte';
    import P2Age from './P2Age.svelte';
    import P3Class from './P3Class.svelte';
    import axios from 'axios';
    import ResultPage from './ResultPage.svelte';
    
    const pages = [P1Gender, P2Age, P3Class];
  
    // The current page of our form.
    let page = 0;
  
    // The state of all of our pages
    let pagesState = [];

    let result = null;
    let result2 = null;  

    // Our handlers
    async function onSubmit(values) {
      if (page === pages.length - 1) {
        // On our final page with POST our data somewhere
        pagesState[page] = values;
        pagesState = pagesState; // Triggering update

        await doPost();
      } else {
        // If we're not on the last page, store our data and increase a step
        pagesState[page] = values;
        pagesState = pagesState; // Triggering update
        page +=1;
      }
    }

    async function doPost () {
        axios.post('http://localhost:5000/api/predict', {
            passengerClass: Number(pagesState[2].selectedClass),
            male: pagesState[0].Gender === 'true' ? true : false,
            age: pagesState[1].selectedAge
        })
        .then(function (response) {
            console.log(response);
            result = JSON.stringify(response.data.survived)
            if (result == 0)
              {
                result = "You died"
              }
            if(result == 1)
              {
                result = "You Survived"
              }
            result2 = JSON.stringify(response.data.survivedProbability)
            console.log(result);
        })
        .catch(function (error) {
            console.log(error);
        });	
	}
  
    function onBack(values) {
      if (page === 0) return;
          pagesState[page] = values;
      pagesState = pagesState; // Triggering update
      page -= 1;
    }

    function onRestart(){
        result = null;
        page = 0;
        pagesState = [];
    }
  </script>
  
  <!-- We display the current step here -->
  {#if result == null}
  <svelte:component
    this={pages[page]}
    {onSubmit}
    {onBack}
    initialValues={pagesState[page]}
    pagesState={pagesState}
    />
    {/if}

    {#if result != null}
        <ResultPage 
        {onRestart}
        result={result}
        result2={result2}/>
    {/if}

    