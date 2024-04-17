//
//  HomeView.swift
//  RedBilbiotecas
//
//  Created by Eduardo Santander Restrepo on 11/4/24.
//

import SwiftUI

class Carrels: Identifiable, ObservableObject {
    let id = UUID()
    let carrelNumber: Int
    let hour: String
    let time: Int
    let user: String
    let location: String
    var date: Date
    var available: Bool
    
    init(carrelNumber: Int, hour: String, time: Int, user: String, location: String, date: Date, available: Bool ) {
        self.carrelNumber = carrelNumber
        self.hour = hour
        self.time = time
        self.user = user
        self.location = location
        self.date = date
        self.available = available
    }
    
    func selected() {
        available = false
    }
    
    func selectDate(bookday: Date) {
        date = bookday
    }
//    Añadir funciones para manejar el carrel
}

class Books:  Identifiable, ObservableObject {
    let id = UUID()
    let title: String
    let author: String
    let bookImage: String
    var devolutionDate: String
    var available: Bool
    
    init(title: String, author: String, bookImage: String, devolutionDate: String, available: Bool) {
        self.title = title
        self.author = author
        self.bookImage = bookImage
        self.devolutionDate = devolutionDate
        self.available = available
    }
    
    func selected() {
        available = false
    }
}


struct HomeView: View {
    @Binding var username: String
    @State var carrels: [Carrels] = [
        Carrels(carrelNumber: 1, hour: "10:00", time: 1,  user: "", location: "Escuela Superior Ingeniería y tecnología", date: Date(),  available: true),
        Carrels(carrelNumber: 1, hour: "11:00", time: 1,  user: "", location: "Escuela Superior Ingeniería y tecnología", date: Date(),  available: true),
        Carrels(carrelNumber: 1, hour: "12:00", time: 1,  user: "", location: "Escuela Superior Ingeniería y tecnología", date: Date(),  available: true),
        Carrels(carrelNumber: 2, hour: "10:00", time: 1,  user: "", location: "Escuela Superior Ingeniería y tecnología", date: Date(),  available: true),
        Carrels(carrelNumber: 2, hour: "11:00", time: 1,  user: "", location: "Escuela Superior Ingeniería y tecnología", date: Date(),  available: true),
        Carrels(carrelNumber: 2, hour: "12:00", time: 1,  user: "", location: "Escuela Superior Ingeniería y tecnología", date: Date(),  available: true),
        Carrels(carrelNumber: 3, hour: "10:00", time: 1,  user: "", location: "Escuela Superior Ingeniería y tecnología", date: Date(),  available: true),
        Carrels(carrelNumber: 3, hour: "11:00", time: 1,  user: "", location: "Escuela Superior Ingeniería y tecnología", date: Date(),  available: true),
        Carrels(carrelNumber: 3, hour: "12:00", time: 1,  user: "", location: "Escuela Superior Ingeniería y tecnología", date: Date(),  available: true),
    ]
    @State var books: [Books] = [
        Books(title: "Una historia de España", author: "Arturo Pérez-Reverte", bookImage: "historia", devolutionDate: "21/4/24", available: true),
        Books(title: "UN CAFÉ A SOLAS", author: "MIGUEL ÁNGEL MONTERO", bookImage: "lonely",devolutionDate: "21/4/24", available: true),
        Books(title: "Fundamentos de los Requisitos de Software", author: "Jorge Bernal García", bookImage: "software", devolutionDate: "21/4/24",available: true),
        Books(title: "Tres enigmas para la Organización", author: "Eduardo Mendoza", bookImage: "enigma", devolutionDate: "21/4/24", available: true),
        Books(title: "LA ÚLTIMA FUNCIÓN", author: "Luis Landero", bookImage: "function",devolutionDate: "21/4/24", available: true),
    ]
    var body: some View {
        TabView {
            BookView(books: $books)
                .tabItem {
                    Image(systemName: "book")
                    Text("Libros")
                }
            BookRoomView(carrels: $carrels)
                .tabItem {
                    Image(systemName: "studentdesk")
                    Text("Espacios")
                }
            MyBooksView(carrels: $carrels, books: $books)
                .tabItem {
                    Image(systemName: "tray.fill")
                    Text("Reservas")
                }
            ProfileView(username: $username)
                .tabItem {
                    Image(systemName: "person.crop.circle.fill")
                    Text("Perfil")
                }
        }
        .background(Color("Background"))
    }
}

struct BookView: View {
    @State private var searchText = ""
    @State private var showResults : Bool = false
    @Binding var books: [Books]
    
    var body: some View {
        VStack {
            VStack (alignment: .leading) {
                HStack {
                    Text("Reservar libros")
                        .font(.title)
                        .fontWeight(.black)
                        .fontDesign(.rounded)
                        .padding(.top, 30)
                    Spacer()
                }
                .padding(.horizontal, 30)
            }
                VStack {
                    ZStack {
                      RoundedRectangle(cornerRadius: 15)
                            .stroke(.accent, lineWidth: 3)
                            .frame(width: 340, height: 60)
                        HStack {
                            Image(systemName: "magnifyingglass")
                            TextField("Search", text: $searchText)
                                
                        }
                        .padding(.horizontal, 20)
                    }
                    .padding(.horizontal, 30)
                    .padding()
                    HStack {
                        if showResults {
                            Text("Libros encontrados")
                                .fontWeight(.bold)
                                .font(.title3)
                        } else {
                            Text("Lista de libros")
                                .fontWeight(.bold)
                                .font(.title3)
                        }
                        Spacer()
                            Button(action: {
                                showResults.toggle()
                            }) {
                                ZStack {
                                    RoundedRectangle(cornerRadius: 30)
                                        .foregroundStyle(showResults ? .gray : .accent)
                                        .frame(width: 120, height: 40)
                                    Text(showResults ? "Volver" : "Buscar")
                                        .foregroundStyle(.white)
                                        .fontWeight(.bold)
                                }
                            }
                    }
                    .padding(.horizontal, 30)
                }
            if showResults {
                VStack (alignment: .leading) {
                    ScrollView {
                        ScrollView {
                            ForEach($books) { $book in
                                BookListView(book: book,available: $book.available)
                            }
                        }
                        .scrollIndicators(.hidden)
                        .padding()
                    }
                }
            } else {
                ScrollView {
                    
            }
            }
        }
        .background(Color("Background"))
    }
}

struct BookRoomView: View {
    @State private var bookday = Date()
    @State private var showResults : Bool = false
    @Binding var carrels: [Carrels]
    
    var body: some View {
        VStack {
            VStack (alignment: .leading){
                HStack {
                    Text("Reservar espacios")
                        .font(.title)
                        .fontWeight(.black)
                        .fontDesign(.rounded)
                        .padding(.top, 30)
                    Spacer()
                }
                .padding(.horizontal, 30)
            }
            VStack {
                ZStack {
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(.accent, lineWidth: 3)
                        .frame(width: 340, height: 60)
                    HStack {
                        DatePicker(selection: $bookday,
                                   displayedComponents: .date,
                                   label: {
                            HStack {
                                if !showResults {
                                    Image(systemName: "calendar")
                                        .foregroundStyle(.gray)
                                }
                                Text(showResults ? "Reserva para el" :"Elige la fecha")
                                    .fontDesign(.rounded)
                            }
                        })
                    }
                    .padding(.horizontal, 20)
                }
                .padding(.horizontal, 30)
                .padding()
                HStack {
                    if showResults {
                        Text("Disponibilidad")
                            .fontWeight(.bold)
                            .font(.title3)
                    }
                    Spacer()
                        Button(action: {
                            showResults.toggle()
                        }) {
                            ZStack {
                                RoundedRectangle(cornerRadius: 30)
                                    .foregroundStyle(showResults ? .gray : .accent)
                                    .frame(width: 120, height: 40)
                                Text(showResults ? "Volver" : "Buscar")
                                    .foregroundStyle(.white)
                                    .fontWeight(.bold)
                            }
                        }
                }
                .padding(.horizontal, 30)
            }
            if showResults {
                ScrollView {
                    ForEach($carrels) { $carrel in
                        CarrelListView(carrel: carrel,available: $carrel.available,  bookday: $bookday)
                    }
                }
                .scrollIndicators(.hidden)
                .padding()
            } else {
                ScrollView {
                    
                }
            }
        }
        .background(Color("Background"))
    }
}


struct MyBooksView: View {
    @Binding var carrels: [Carrels]
    @Binding var books: [Books]
    @State private var showLibros: Bool = true
    @State private var showCarrels: Bool = false
    
    var dateFormatter: DateFormatter {
        let formatter = DateFormatter()
        formatter.dateFormat = "dd/MM/yyyy" // Formato de fecha deseado
        return formatter
    }
    
    
    var body: some View {
        VStack {
            VStack (alignment: .leading) {
                HStack {
                    Text("Mis reservas")
                        .font(.title)
                        .fontWeight(.black)
                        .fontDesign(.rounded)
                        .padding(.top, 30)
                    Spacer()
                }
                .padding(.horizontal, 30)
                HStack {
                    Button(action: {
                        showLibros = true
                        showCarrels = false
                    }) {
                        Text("Libros")
                            .padding(10)
                            .padding(.horizontal, 10)
                            .background(showLibros ? .accent : .gray)
                            .foregroundStyle(.white)
                            .fontWeight(.bold)
                            .cornerRadius(30)
                    }
                    .padding(.leading, 30)
                    Button(action: {
                        showCarrels = true
                        showLibros = false
                    }) {
                        Text("Carrels")
                            .padding(10)
                            .padding(.horizontal, 10)
                            .background(showCarrels ? .accent : .gray)
                            .foregroundStyle(.white)
                            .fontWeight(.bold)
                            .cornerRadius(30)
                    }
                    Spacer()
                }
                if showLibros {
                    ScrollView {
                        ForEach($books) { $book in
                            if !book.available {
                                VStack {
                                    ZStack (alignment: .leading) {
                                        RoundedRectangle(cornerRadius: 15)
                                            .frame(width: 340, height: 160)
                                            .foregroundStyle(.accent)
                                        HStack {
                                            VStack (alignment: .leading) {
                                                Text("Libro \(book.title) prestado")
                                                Text("Autor \(book.author)")
                                                Text("Dia Entrega: \(book.devolutionDate)")
                                            }
                                            .fontDesign(.rounded)
                                            .font(.headline)
                                            .foregroundStyle(.white)
                                            .padding(.leading, 20)
                                            Spacer()
                                            Button(action: {
                                            }) {
                                                Text("Devolver")
                                                    .padding(6)
                                                    .padding(.horizontal, 7)
                                                    .background(.red)
                                                    .foregroundStyle(.white)
                                                    .cornerRadius(30)
                                            }
                                            .padding(.trailing, 45)
                                        }
                                    }
                                    .padding(.top, 10)
                                    .padding(.leading, 30)
                                }
                            }
                        }
                    }
                    .padding(.bottom, 15)
                } else {
                    ScrollView {
                        ForEach($carrels) { $carrel in
                            if !carrel.available {
                                VStack {
                                    ZStack (alignment: .leading) {
                                        RoundedRectangle(cornerRadius: 15)
                                            .frame(width: 340, height: 120)
                                            .foregroundStyle(.accent)
                                        HStack {
                                            VStack (alignment: .leading) {
                                                Text("Carrel \(carrel.carrelNumber) reservado")
                                                Text("Duracion: \(carrel.time) hora")
                                                Text("Hora: \(carrel.hour)")
                                                HStack {
                                                    Text("Dia: \(dateFormatter.string(from: carrel.date))")
                                                }
                                            }
                                            .fontDesign(.rounded)
                                            .font(.headline)
                                            .foregroundStyle(.white)
                                            .padding(.leading, 20)
                                            Spacer()
                                            Button(action: {
                                            }) {
                                                Text("Cancelar")
                                                    .padding(6)
                                                    .padding(.horizontal, 7)
                                                    .background(.red)
                                                    .foregroundStyle(.white)
                                                    .cornerRadius(30)
                                            }
                                            .padding(.trailing, 45)
                                        }
                                    }
                                    .padding(.top, 10)
                                    .padding(.leading, 30)
                                }
                            }
                        }
                    }
                    .padding(.bottom, 15)
                }
            }
        }
        .background(Color("Background"))
    }
}

struct ProfileView: View {
    @Binding var username: String
    var body: some View {
        VStack {
            VStack (alignment: .leading) {
                HStack {
                    Text("Perfil")
                        .font(.title)
                        .fontWeight(.black)
                        .fontDesign(.rounded)
                        .padding(.top, 30)
                    Spacer()
                }
                VStack (alignment: .leading) {
                    ZStack (alignment: .leading) {
                        RoundedRectangle(cornerRadius: 15)
                            .stroke(.accent, lineWidth: 3)
                            .frame(width: 350, height: 60)
                        HStack {
                            Text("Username:")
                            Text("\(username)")
                                .fontWeight(.regular)
                        }
                        .padding(.leading, 15)
                    }
                    ZStack (alignment: .leading) {
                        RoundedRectangle(cornerRadius: 15)
                            .stroke(.accent, lineWidth: 3)
                            .frame(width: 350, height: 60)
                        HStack {
                            Text("Alu:")
                            Text("alu0101565590")
                                .fontWeight(.regular)
                        }
                        .padding(.leading, 15)
                    }
                }
                .font(.title2)
                .fontWeight(.bold)
                .fontDesign(.rounded)
                .padding(.top, 10)
            }
            .padding(.horizontal, 30)
            ScrollView {
                
            }
        }
        .background(Color("Background"))
    }
}


struct BookListView: View {
    @State var book: Books
    @Binding var available: Bool
    @State private var showingSheet: Bool = false
    
    var body: some View {
            HStack {
                ZStack (alignment: .leading) {
                        RoundedRectangle(cornerRadius: 15)
                            .stroke(book.available ? .accent : .gray, lineWidth: 3)
                            .frame(width: 230, height: 80)
                        VStack {
                            Text("\(book.title)")
                                .fontDesign(.rounded)
                                .lineLimit(2)
                        }
                        .frame(width: 100, height: 50)
                        .padding(.leading, 30)
                    }
                    Button(action: {
                        if !book.available {
                            
                        } else {
                            showingSheet = true
                        }
                    }) {
                        VStack {
                            ZStack {
                                RoundedRectangle(cornerRadius: 15)
                                    .foregroundStyle(book.available ? .accent : .gray)
                                    .frame(width: 100, height: 30)
                                Text("Reservar")
                                    .foregroundStyle(.white)
                                    .fontWeight(.bold)
                            }
                        }
                        
                    }
                }
            .frame(width: 400, height: 120)
                .sheet(isPresented: $showingSheet) {
                    ZStack {
                        Color.accent.ignoresSafeArea() // Change this to the desired background color
                        Overlay2View(book: book, showingSheet: $showingSheet, available: $available)
                            .presentationDetents([.fraction(0.30)])
                            .presentationDragIndicator(.visible)
                            .presentationCornerRadius(25)
                    }
                }
    }
}

struct CarrelListView: View {
    @State var carrel: Carrels
    @Binding var available: Bool
    @State private var showingSheet: Bool = false
    @Binding var bookday: Date
    
    var body: some View {
            HStack {
                    ZStack {
                        RoundedRectangle(cornerRadius: 15)
                            .stroke(carrel.available ? .accent : .gray, lineWidth: 3)
                            .frame(width: 230, height: 50)
                        HStack {
                            Text("Carrel \(carrel.carrelNumber)")
                                .padding(.trailing, 90)
                                .fontDesign(.rounded)
                            Text(carrel.hour)
                        }
                    }
                    Button(action: {
                        if !carrel.available {
                            
                        } else {
                            showingSheet = true
                        }
                    }) {
                        VStack {
                            ZStack {
                                RoundedRectangle(cornerRadius: 15)
                                    .foregroundStyle(carrel.available ? .accent : .gray)
                                    .frame(width: 100, height: 30)
                                Text("Reservar")
                                    .foregroundStyle(.white)
                                    .fontWeight(.bold)
                            }
                        }
                        
                    }
                }
            .frame(width: 400, height: 60)
                .sheet(isPresented: $showingSheet) {
                    ZStack {
                        Color.accent.ignoresSafeArea() // Change this to the desired background color
                        OverlayView(carrel: carrel, bookday: $bookday, showingSheet: $showingSheet, available: $available)
                            .presentationDetents([.fraction(0.38)])
                            .presentationDragIndicator(.visible)
                            .presentationCornerRadius(25)
                    }
                }
    }
}

struct OverlayView: View {
    @State var carrel: Carrels
    @Binding var bookday: Date
    @Binding var showingSheet: Bool
    @Binding var available: Bool
    @State private var confirm: Bool = false
    
    var dateFormatter: DateFormatter {
        let formatter = DateFormatter()
        formatter.dateFormat = "dd/MM/yyyy" // Formato de fecha deseado
        return formatter
    }
    
    var body: some View {
        HStack {
            VStack {
                VStack (alignment: .leading) {
                    Text("Reservar Carrel \(carrel.carrelNumber)")
                        .font(.title2)
                        .fontWeight(.bold)
                        .foregroundStyle(.white)
                        .padding(.bottom, 5)
                    Label("Hora: \(carrel.hour)", systemImage: "clock")
                        .font(.title3)
                        .foregroundStyle(.white)
                        .padding(.top, 1)
                        .padding(.horizontal, 3)
                    Label("Dia: \(dateFormatter.string(from: bookday))", systemImage: "calendar")
                        .font(.title3)
                        .foregroundStyle(.white)
                        .padding(.top, 1)
                        .padding(.horizontal, 4)
                    Label("Tiempo: \(carrel.time) hora", systemImage: "clock.arrow.circlepath")
                        .font(.title3)
                        .foregroundStyle(.white)
                        .padding(.top, 1)
                        .padding(.horizontal, 3)
                    Label("Lugar: \(carrel.location)", systemImage: "location.fill")
                        .font(.title3)
                        .foregroundStyle(.white)
                        .padding(.top, 1)
                        .padding(.horizontal, 3)
                        .lineLimit(1)
                    Spacer()

                }
                .padding(.top, 30)
                Button(action: {
                    confirm = true
                    carrel.selected()
                    available = false
                    carrel.selectDate(bookday: bookday)
                    DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
                         showingSheet = false
                    }
                }) {
                    ZStack {
                        RoundedRectangle(cornerRadius: 30)
                            .foregroundStyle(.white)
                            .frame(width: 200, height: 45)
                        if confirm {
                            Label("Reserva realizada", systemImage: "checkmark")
                                .foregroundStyle(.green)
                                .fontWeight(.bold)
                        } else {
                            Text("Confirmar reserva")
                                .foregroundStyle(.black)
                                .fontWeight(.bold)
                        }
                    }
                }
                .padding(.bottom, 10)
            }
            Spacer()
        }
        .padding(.horizontal, 30)
    }
}

struct Overlay2View: View {
    @State var book: Books
    @Binding var showingSheet: Bool
    @Binding var available: Bool
    @State private var confirm: Bool = false
    
    var dateFormatter: DateFormatter {
        let formatter = DateFormatter()
        formatter.dateFormat = "dd/MM/yyyy" // Formato de fecha deseado
        return formatter
    }
    
    var body: some View {
        HStack {
            VStack {
                VStack (alignment: .leading) {
                    Text("Prestar \(book.title)")
                        .font(.title2)
                        .fontWeight(.bold)
                        .foregroundStyle(.white)
                        .padding(.bottom, 5)
                    Label("Author: \(book.author)", systemImage: "person")
                        .font(.title3)
                        .foregroundStyle(.white)
                        .padding(.top, 1)
                        .padding(.horizontal, 3)
                    Label("Dia: \(book.devolutionDate)", systemImage: "calendar")
                        .font(.title3)
                        .foregroundStyle(.white)
                        .padding(.top, 1)
                        .padding(.horizontal, 4)
                    Spacer()

                }
                .padding(.top, 30)
                Button(action: {
                    confirm = true
                    book.selected()
                    available = false
                    DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
                         showingSheet = false
                    }
                }) {
                    ZStack {
                        RoundedRectangle(cornerRadius: 30)
                            .foregroundStyle(.white)
                            .frame(width: 200, height: 45)
                        if confirm {
                            Label("Reserva realizada", systemImage: "checkmark")
                                .foregroundStyle(.green)
                                .fontWeight(.bold)
                        } else {
                            Text("Confirmar reserva")
                                .foregroundStyle(.black)
                                .fontWeight(.bold)
                        }
                    }
                }
                .padding(.bottom, 10)
            }
            Spacer()
        }
        .padding(.horizontal, 30)
    }
}
