class University{
    constructor(name, departments){
        this.name=name;
        this.departments=departments;
    }
    displayDepartments(){
        console.log("\nDepartments in " + this.name + ":");
        for(let i = 0; i < this.departments.length; i++) {
            console.log(`${i+1}. ${this.departments[i]}`);
        }
    }
    addDepartment(department){
        this.departments.push(department);
        console.log(`\nDepartment "${department}" added to ${this.name}.`);
    }
    removeDepartment(department){
        let idx=this.departments.indexOf(department);
        if(idx !== -1){
            this.departments.splice(idx, 1);
            console.log(`\nDepartment "${department}" removed from ${this.name}.`);
        } else {
            console.log(`\nDepartment "${department}" not found in ${this.name}.`);
        }
    }
}

let university= new University("Gujarat Technological University", ["Computer Engg.", "Information Technology", "Robotics and Automation", "Electronics and Communication"]);
university.displayDepartments();

university.addDepartment("Biomedical Engineering");
university.displayDepartments();

university.removeDepartment("Robotics and Automation");
university.displayDepartments();