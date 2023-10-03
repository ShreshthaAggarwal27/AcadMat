$(document).ready(function() {
    // Define the options for school grades and college years
    var schoolGrades = ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"];
    var collegeYears = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"];
    
    // Function to update the "grade_year" select field
    function updateGradeYearOptions() {
        var level = $("#level").val();
        var gradeYearSelect = $("#grade_year");
        gradeYearSelect.empty(); // Clear existing options

        // Add options based on the selected level
        var options = level === "school" ? schoolGrades : collegeYears;
        $.each(options, function(index, value) {
            gradeYearSelect.append($("<option>").text(value).val(value));
        });
    }
    
    // Initial setup
    updateGradeYearOptions();
    
    // Listen for changes in the "level" select field
    $("#level").change(function() {
        updateGradeYearOptions();
    });
});