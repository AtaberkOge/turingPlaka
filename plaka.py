class TuringMachine:
    def __init__(self, plaka):
        self.tape = list(plaka) + ['_'] # '_' boşluk karakterini temsil eder
        self.head_position = 0
        self.current_state = 'q0' # Başlangıç durumu
        self.transitions = {}
        
        self.setup_transitions()

    def setup_transitions(self):
        digits = "0123456789"
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # q0 -> ilk rakam
        for d in digits:
            self.transitions[('q0', d)] = ('q1', d, 'R')
            
        # q1 -> ikinci rakam
        for d in digits:
            self.transitions[('q1', d)] = ('q2', d, 'R')
            
        # q2 -> ilk harf
        for l in letters:
            self.transitions[('q2', l)] = ('q3', l, 'R')
            
        # q3 -> ikinci harf
        for l in letters:
            self.transitions[('q3', l)] = ('q4', l, 'R')
            
        # q4 -> ilk rakam (üçüncü rakam öbeğinin başı)
        for d in digits:
            self.transitions[('q4', d)] = ('q5', d, 'R')
            
        # q5 -> ikinci rakam (üçüncü rakam öbeğinin ortası)
        for d in digits:
            self.transitions[('q5', d)] = ('q6', d, 'R')
            
        # q6 -> üçüncü rakam (son rakam)
        for d in digits:
            self.transitions[('q6', d)] = ('q7', d, 'R')
            
        # q7 -> kabul durumu (tam olarak 7 karakter olmasını sağlamak için boşluk bekler)
        self.transitions[('q7', '_')] = ('KABUL_DURUMU', '_', 'S') # S: Sabit/Dur

    def run(self):
        print("\n--- Turing Makinesi Çalışmaya Başlıyor ---")
        
        while True:
            read_symbol = self.tape[self.head_position]
            state_symbol_pair = (self.current_state, read_symbol)
            
            # Her adımda çıktı 
            bant_icerigi = "".join(self.tape)
            print(f"Mevcut durum: {self.current_state} | Okunan: {read_symbol} | Bant: {bant_icerigi} | Kafa Pozisyonu: {self.head_position}")
            
            # Kabul durumu kontrolü
            if self.current_state == 'KABUL_DURUMU':
                print("Sonuç: KABUL") #
                break
                
            
            if state_symbol_pair in self.transitions:
                next_state, write_symbol, move_dir = self.transitions[state_symbol_pair]
                
                # Bandı güncelle
                self.tape[self.head_position] = write_symbol
                self.current_state = next_state
                
                # Kafayı hareket ettir
                print(f"Kafa Hareketi: {move_dir}\n")
                if move_dir == 'R':
                    self.head_position += 1
                elif move_dir == 'L':
                    self.head_position -= 1
                    
            else:

                print("Sonuç: RED") 
                break

# input
if __name__ == "__main__":
    print("Örnek Geçerli Girdiler: 55AB123, 34TR456, 06AA789")
    print("Örnek Geçersiz Girdiler: 5AB123, 555AB12, 34A1234, 55ab123 vs.")
    kullanici_girdisi = input("Lütfen kontrol edilecek plakayı girin: ")
    
    tm = TuringMachine(kullanici_girdisi)
    tm.run()