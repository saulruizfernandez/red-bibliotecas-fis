//
//  LoginView.swift
//  RedBilbiotecas
//
//  Created by Eduardo Santander Restrepo on 11/4/24.
//

import SwiftUI

struct LoginView: View {
    @State  var name : [String] = ["Usuario", "Contraseña"]
    @State var boxContent : [String] = ["Nombre de usuario", "Contraseña", "Iniciar Sesión"]
    @State var isSelected: Bool = true
    @State var isSelected2: Bool = false
    @State var mainView: Bool = false
    @State var username: String = ""
    var body: some View {
        if !mainView {
            VStack {
                TitleView()
                BoxView(name: $name[0], boxContent: $boxContent[0], isSelected: $isSelected, isSelected2: $isSelected2, username: $username)
                Box2View(name: $name[1], boxContent: $boxContent[1], isSelected2: $isSelected2, isSelected: $isSelected)
                LoginBoxView(name: $name[1], boxContent: $boxContent[2], loginView: $mainView)
                Divider()
                    .padding()
                HStack {
                    Text("¿No tienes cuenta?")
                    Text("Crear cuenta")
                        .foregroundStyle(.accent)
                }
                .padding(.top, 30)
                Spacer()
                Image("LogoULL")
            }
            .background(Color("Background"))
        } else {
            HomeView(username: $username)
        }
    }
}

#Preview {
    LoginView()
}

struct TitleView: View {
    var body: some View {
        VStack {
            Text("Iniciar sesión")
                .font(.title)
                .fontWeight(.black)
                .fontDesign(.rounded)
            Text("Encantados de verte de nuevo")
                .font(.subheadline)
                .fontWeight(.semibold)
                .fontDesign(.rounded)
        }
        .padding(.top, 50)
        .padding(.bottom, 40)
    }
}

struct BoxView: View {
    @Binding var name : String
    @Binding var boxContent : String
    @Binding var isSelected: Bool
    @Binding var isSelected2: Bool
    @Binding var username: String
    
    var body: some View {
        VStack (alignment: .leading) {
            Text(name)
                .fontDesign(.rounded)
                .fontWeight(.bold)
                .padding(.top, 7)
                .padding(.horizontal, 30)
                ZStack {
                  RoundedRectangle(cornerRadius: 15)
                        .stroke(.accent, lineWidth: 3)
                        .frame(width: 340, height: 60)
                    HStack {
                        Image(systemName: "person.fill")
                        TextField(boxContent, text: $username)
                    }
                    .padding(.horizontal, 20)
                }
                .padding(.horizontal, 30)
        }
        .padding(.horizontal, 30)
    }
}

struct Box2View: View {
    @Binding var name : String
    @Binding var boxContent : String
    @Binding var isSelected2: Bool
    @Binding var isSelected: Bool
    @State private var password: String = ""
    
    var body: some View {
        VStack (alignment: .leading) {
            Text(name)
                .fontDesign(.rounded)
                .fontWeight(.bold)
                .padding(.top, 7)
                .padding(.horizontal, 30)
            VStack (alignment: .trailing) {
                ZStack {
                  RoundedRectangle(cornerRadius: 15)
                        .stroke(.accent, lineWidth: 3)
                        .frame(width: 340, height: 60)
                    HStack {
                        Image(systemName: "key.fill")
                        SecureField(boxContent, text: $password)
                    }
                    .padding(.horizontal, 20)
                }
                .padding(.horizontal, 30)
                Text("¿Olvidaste tu contraseña?")
                    .foregroundStyle(.accent)
                    .fontDesign(.rounded)
                    .fontWeight(.light)
                    .font(.subheadline)
                    .padding(.top, 5)
                    .padding(.horizontal, 30)
            }

        }
    }
}

struct LoginBoxView: View {
    @Binding var name : String
    @Binding var boxContent : String
    @Binding var loginView : Bool
    @State var isSelected: Bool = false
    @State private var loading: Bool = false
    
    var body: some View {
        VStack (alignment: .leading) {
            Button(action: {
                loading = true
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                    loginView = true
                }
            }) {
                ZStack {
                    RoundedRectangle(cornerRadius: 25)
                        .foregroundStyle(.accent)
                        .frame(width: 320, height: 50)
                        .shadow(radius: 1)
                    if loading {
                        Label("Iniciando sesion", systemImage: "circle.dotted")
                            .foregroundStyle(.white)
                            .font(.headline)
                    } else {
                        Text(boxContent)
                            .foregroundStyle(.white)
                            .font(.headline)
                    }
                }
            }
        }
        .padding(.top, 15)
    }
}
