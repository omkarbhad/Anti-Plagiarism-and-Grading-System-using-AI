function check1() {

    checktype = document.getElementById("inputGroupSelect04");
    essay = document.getElementById("textbox");

    custom_marks_checkbox = document.getElementById("markscheck");
    custom_marks_input = document.getElementById("marksinput");

    console.log(checktype.value)
    console.log(essay.value)
    console.log(custom_marks_checkbox.checked)
    console.log(custom_marks_input.value)

    if ((essay.value.length) < 10) {
        alert("Essay too small !!")
        return
    }

    if (checktype.value == "Choose...") {
        alert("Choose an Option")
        return
    }

    if (custom_marks_checkbox.checked == true) {
        if (!custom_marks_input.value) {
            alert("Oops, Did you forget to enter marks?")
            return
        }
        if (custom_marks_input.value == 0) {
            alert("Marks can't be zero!!")
            return
        }
        if (custom_marks_input.value > 1000) {
            alert("Marks value too high!!")
            return
        }
    }

    $('#loadMe').modal('show');

    if (checktype.value == 1) {

        var data = new FormData();
        data.append("string", essay.value);

        if (custom_marks_checkbox.checked == true) {
            data.append("custom_marks", custom_marks_input.value)
            localStorage.setItem("custom_marks", custom_marks_input.value);
        } else {
            data.append("custom_marks", 100)
            localStorage.setItem("custom_marks", 100);
        }

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function() {
            if (this.readyState === 4) {

                console.log(this.responseText);

                localStorage.setItem("grade", this.responseText);
                $('#loadMe').modal('hide');
                window.location.href = 'http://127.0.0.1:8000/graderesult/'

            }
        });

        xhr.open("POST", "http://127.0.0.1:8000/grade/");

        xhr.send(data);
        return

    }



    if (checktype.value == 2) {

        var data = new FormData();
        data.append("string", essay.value);

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function() {
            if (this.readyState === 4) {

                console.log(this.responseText);

                localStorage.setItem("validate", this.responseText);
                $('#loadMe').modal('hide');
                window.location.href = 'http://127.0.0.1:8000/validateresult/'

            }
        });

        xhr.open("POST", "http://127.0.0.1:8000/validate/");

        xhr.send(data);
        return

    }

    if (checktype.value == 3) {

        var data = new FormData();
        data.append("string", essay.value);

        if (custom_marks_checkbox.checked == true) {
            data.append("custom_marks", custom_marks_input.value)
            localStorage.setItem("custom_marks", custom_marks_input.value);
        } else {
            data.append("custom_marks", 100)
            localStorage.setItem("custom_marks", 100);
        }

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function() {
            if (this.readyState === 4) {

                console.log(this.responseText);

                localStorage.setItem("grade", this.responseText);

            }
        });

        xhr.open("POST", "http://127.0.0.1:8000/grade/");

        xhr.send(data);


        var data = new FormData();
        data.append("string", essay.value);

        var xhr = new XMLHttpRequest();
        xhr.withCredentials = true;

        xhr.addEventListener("readystatechange", function() {
            if (this.readyState === 4) {

                console.log(this.responseText);

                localStorage.setItem("validate", this.responseText);
                window.location.href = 'http://127.0.0.1:8000/both/'

            }
        });

        xhr.open("POST", "http://127.0.0.1:8000/validate/");

        xhr.send(data);

        return

    }


}