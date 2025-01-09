use inquire::Select;
use crate::modules::exit::{ExitChoices, close_program};
use crate::constants::packages::{HYPERLAND_PACKAGES, QTILE_PACKAGES};
use crate::installations::install_from_pacman::install_from_pacman;


pub fn choices_twm() {
    let choices_twm = vec![
        "bspwm",
        "hyperland",
        "qtile",
        "exit"
    ];

    let choices_twm_ans = Select::new(
        "Which Tiling Window Manager would you like to install?", 
        choices_twm
    ).prompt();

    if let Ok(choice) = choices_twm_ans {
        match choice {
            "bspwm" => println!("bspwm not implemented yet"),
            "hyperland" => install_from_pacman(HYPERLAND_PACKAGES, "hyperland"),
            "qtile" => install_from_pacman(QTILE_PACKAGES, "qtile"),
            "exit" => close_program(ExitChoices::Exit),
            _ => close_program(ExitChoices::InvalidChoice),
        }
    } else {
        close_program(ExitChoices::Error);
    }
}
