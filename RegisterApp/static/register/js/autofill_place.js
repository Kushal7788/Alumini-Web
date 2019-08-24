var placeSearch, autocomplete;

var componentForm = {
    current_city: 'long_name',
    current_state: 'long_name',
    current_country: 'long_name',
};

function initAutocomplete() {
    autocomplete_current = new google.maps.places.Autocomplete(
        //autocomplete_current = new google.maps.places.Autocomplete(
        document.getElementById('current_street_address'), {types: ['geocode']});
    autocomplete_current.setFields(['address_component']);
    autocomplete_current.addListener('place_changed', fillInAddress);


    autocomplete_college = new google.maps.places.Autocomplete(
        document.getElementById('college_city'), {types: ['geocode']});
    autocomplete_college.setFields(['address_component']);
    autocomplete_college.addListener('place_changed', fillInAddress_college);

    autocomplete_work = new google.maps.places.Autocomplete(
        document.getElementById('work_city'), {types: ['geocode']});
    autocomplete_work.setFields(['address_component']);
    autocomplete_work.addListener('place_changed', fillInAddress_work);

    autocomplete_school = new google.maps.places.Autocomplete(
        document.getElementById('school_street_address'), {types: ['geocode']});
    autocomplete_school.setFields(['address_component']);
    autocomplete_school.addListener('place_changed', fillInAddress_school);
}

function fillInAddress() {
    var place = autocomplete_current.getPlace();
    var s = document.getElementById('current_street_address');
    var st = s.value;
    st = st.substring(0, st.indexOf(','))
    s.value = st;
    var len = place.address_components.length;
    String.prototype.isNumber = function () {
        return /^\d+$/.test(this);
    }
    var temp = place.address_components[len - 1]['long_name'].toString();
    if (temp.isNumber()) {
        console.log(temp);
        document.getElementById('current_pincode').value = place.address_components[len - 1]['long_name'];
        len = len - 1;
    }
    document.getElementById('current_country').value = place.address_components[len - 1]['long_name'];
    document.getElementById('current_state').value = place.address_components[len - 2]['long_name'];
    document.getElementById('current_city').value = place.address_components[len - 3]['long_name'];
}

function fillInAddress_college() {
    var place = autocomplete_college.getPlace();
    s = document.getElementById('college_city');
    st = s.value;
    st = st.substring(0, st.indexOf(','))
    s.value = st;
    len = place.address_components.length;
    String.prototype.isNumber = function () {
        return /^\d+$/.test(this);
    }
    var temp = place.address_components[len - 1]['long_name'].toString();
    if (temp.isNumber()) {
        console.log(temp);
        len = len - 1;
    }
    document.getElementById('college_country').value = place.address_components[len - 1]['long_name'];
    document.getElementById('college_state').value = place.address_components[len - 2]['long_name'];
    document.getElementById('college_city').value = place.address_components[len - 3]['long_name'];
}

function fillInAddress_school() {
    var place = autocomplete_school.getPlace();
    s = document.getElementById('school_street_address');
    st = s.value;
    st = st.substring(0, st.indexOf(','))
    s.value = st;
    len = place.address_components.length;
    String.prototype.isNumber = function () {
        return /^\d+$/.test(this);
    }
    var temp = place.address_components[len - 1]['long_name'].toString();
    if (temp.isNumber()) {
        console.log(temp);
        len = len - 1;
    }
    document.getElementById('school_city').value = place.address_components[len - 3]['long_name'];
    document.getElementById('school_state').value = place.address_components[len - 2]['long_name'];
    document.getElementById('school_country').value = place.address_components[len - 1]['long_name'];
}


function fillInAddress_work() {
    var place = autocomplete_work.getPlace();
    s = document.getElementById('work_city');
    st = s.value;
    st = st.substring(0, st.indexOf(','));
    s.value = st;
    len = place.address_components.length;
    String.prototype.isNumber = function () {
        return /^\d+$/.test(this);
    }
    var temp = place.address_components[len - 1]['long_name'].toString();
    if (temp.isNumber()) {
        console.log(temp);

        len = len - 1;
    }

    document.getElementById('work_country').value = place.address_components[len - 1]['long_name'];
    document.getElementById('work_state').value = place.address_components[len - 2]['long_name'];
    document.getElementById('work_city').value = place.address_components[len - 3]['long_name'];
}