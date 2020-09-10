let hatred = document.getElementById("hatred");
hatred.addEventListener("change", () => {
    // Get value from select option
    let seltectedHatred = hatred.options[hatred.selectedIndex].value;

    // Pass option value to tensorflow.js
    //   detectHatred(seltectedHatred);

    // adapt tensorflow.js on chrome tab
    changeContent();
});

// function detectHatred(filter) {
//     return();
//   };

function changeContent(e) {
    chrome.tabs.executeScript({
        file: "filter.js"
    });
};