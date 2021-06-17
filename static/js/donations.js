"use strict";

// Show item search results

function displayItems(results) {
  $("#searched-item-info").html(results);
}

function showItems(evt) {
  evt.preventDefault();

  let url = "/test.json"; 
  let formData = {"searched-item": $("#item-field").val()};

  $.get(url, formData, displayItems); 

}

  $("#search-form").on('submit', showItems);
