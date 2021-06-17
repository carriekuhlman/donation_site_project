"use strict";

// Show item search results

function displayItems(res) {
  // $("#searched-item-info").html(results);
  $("#item-name").text("This");
  $("#item-id").text("Is");
  $("#item-qty").text("Working");
}

function showItems(evt) {
  evt.preventDefault();

  let url = "/test.json"; 
  let formData = {"searched-item": $("#item-field").val()};

  $.get(url, formData, displayItems); 

}

  $("#search-form").on('submit', showItems);
