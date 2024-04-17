//
//  BiblioView.swift
//  RedBilbiotecas
//
//  Created by Eduardo Santander Restrepo on 10/4/24.
//

import SwiftUI

struct BiblioView: View {
    var body: some View {
        VStack (alignment: .leading) {
            HStack {
                Text("Books")
                    .font(.title)
                    .fontWeight(.black)
                Spacer()
            }
            .padding(.top, 30)
            VStack {
                HStack {
                    ExtractedView2()
                    ExtractedView2()
                }
                HStack {
                    ExtractedView2()
                    ExtractedView2()
                }
            }
            Spacer()
        }
        .padding(.horizontal, 30)
    }
}

#Preview {
    BiblioView()
}

struct ExtractedView2: View {
    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 15)
                .frame(width: 350/2, height: 125)
                .foregroundStyle(.accent)
            Text("libro")
                .foregroundStyle(.white)
                .font(.title2)
                .bold()
        }
    }
}
