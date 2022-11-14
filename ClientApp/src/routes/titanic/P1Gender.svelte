<script>
    import { createForm } from 'felte'

    export let initialValues;
	export let onSubmit;

    let gender = true;

    const { form } = createForm({ onSubmit, initialValues })
</script>

<form use:form>
    <h2 style="margin-bottom: 60px">Sex</h2>

    <div style="margin-bottom: 30px">
	<label>
		<input name='Gender' type=radio bind:group={gender} value={true}>
        <img src="MaleIcon.png" alt="Male gender icon" style="width:300px; height:300px; border-radius: 25px; margin-right: 75px">
	</label>

	
	<label>
		<input name='Gender' type=radio bind:group={gender} value={false}>
        <img src="FemaleIcon.png" alt="Male gender icon" style="width:300px; height:300px; border-radius: 25px" >
	</label>
    </div>
    <button class="next" type=submit>Next page</button>

</form>

<style>
    [type=radio] { 
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

/* IMAGE STYLES */
[type=radio] + img {
  cursor: pointer;
}

/* CHECKED STYLES */
[type=radio]:checked + img {
  outline: 2px solid #000000;
}
</style>

