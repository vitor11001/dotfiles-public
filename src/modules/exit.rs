pub enum ExitChoices {
    InvalidChoice,
    Exit,
    Error,
}


pub fn close_program (exit_choice: ExitChoices) {
    match exit_choice {
        ExitChoices::InvalidChoice => println!("Invalid choice, exiting."),
        ExitChoices::Exit => println!("Exiting."),
        ExitChoices::Error => println!("An error occurred, exiting."),
    }
    std::process::exit(0);
}
