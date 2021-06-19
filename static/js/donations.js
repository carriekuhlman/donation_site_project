"use strict";

// Change create account options depending on radio
// button selection

$(document).ready(function(){
  
  $('input[type=radio][name=acct_type]').change(function() {
      if (this.value == "donor_acct") {
        $('.donor-details').show();  
        $('.org-details').hide();
      }else if (this.value == "org_acct") {
        $('.org-details').show();  
        $('.donor-details').hide();
      }
  });

});

// Show donation hours option if selected

$(document).ready(function(){
  
  $('input[type=radio][name=in_person]').change(function() {
      if (this.value == "True") {
        $('.location-donation-hours').show();  
      }else if (this.value == "False") {
        $('.location-donation-hours').hide(); 
      }
  });

});

// Dismissing popovers

$('.popover-dismiss').popover({
  trigger: 'focus'
})

// Modals

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})


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

