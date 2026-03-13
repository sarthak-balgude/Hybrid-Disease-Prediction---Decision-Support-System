
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        display: ['Space Grotesk', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            dark: '#0B1120',
                            accent: '#0ea5e9',
                        }
                    },
                    animation: {
                        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                    }
                }
            }
        }




// --------- Dashboard JS Logic ----------

        function normalizeCommaList(text){
            return text
                .split(',')
                .map(x => x.replace(/[^a-zA-Z0-9\s-]/g, '').trim().toLowerCase())
                .filter(Boolean);
        }

        function uniqueList(arr){
            return [...new Set(arr.map(x => x.toLowerCase()))];
        }

        function setCommaList(list){
            return list.join(', ');
        }

        function setRisk(type, text, signal, desc){
            const dot = document.getElementById('riskDot');
            const textEl = document.getElementById('riskText');
            
            // Base classes for the dot
            let dotClasses = 'w-2.5 h-2.5 rounded-full inline-block shrink-0 transition-colors duration-300 ';
            let textClass = 'text-xs font-bold transition-colors duration-300 ';
            
            if(type === 'ok') {
                dotClasses += 'bg-emerald-500 shadow-[0_0_10px_rgba(16,185,129,0.5)]';
                textClass += 'text-emerald-400';
            } else if(type === 'warn') {
                dotClasses += 'bg-amber-500 shadow-[0_0_10px_rgba(245,158,11,0.5)]';
                textClass += 'text-amber-400';
            } 

            dot.className = dotClasses;
            textEl.className = textClass;
            textEl.textContent = text;
            
            document.getElementById('riskSignal').textContent = signal;
            document.getElementById('riskSignal').className = `text-lg font-display font-bold mt-1 ${
                signal === 'Medium' ? 'text-amber-400' : 'text-emerald-400'
            }`;
            
            document.getElementById('riskDesc').textContent = desc;
        }

        function debounce(func, wait) {
            let timeout;
            return function(...args) {
                clearTimeout(timeout);
                timeout = setTimeout(() => func.apply(this, args), wait);
            };
        }

        function renderTags(){
            const ta = document.getElementById('symptoms');
            const tags = uniqueList(normalizeCommaList(ta.value));
            const panel = document.getElementById('tagPanel');
            
            panel.innerHTML = '';

            if(tags.length === 0) {
                panel.innerHTML = '<span class="text-xs text-slate-600 italic">Awaiting input...</span>';
                document.getElementById('symCount').textContent = '0';
                return;
            }

            tags.forEach(t => {
                const tag = document.createElement('span');
                tag.className = 'inline-flex items-center gap-2 bg-slate-800 border border-slate-700 rounded-md px-3 py-1.5 text-xs text-sky-100 shadow-sm';

                const txt = document.createElement('span');
                txt.textContent = t;

                const btn = document.createElement('button');
                btn.type = "button";
                btn.setAttribute("aria-label", `Remove ${t}`);
                btn.innerHTML = '<i class="fas fa-times"></i>';
                btn.className = 'w-4 h-4 rounded-full bg-slate-700/50 flex items-center justify-center text-[10px] hover:bg-rose-500 hover:text-white text-slate-400 transition ml-1';
                
                btn.addEventListener('click', () => {
                    const updated = tags.filter(x => x !== t);
                    ta.value = setCommaList(updated);
                    renderTags();
                    updateLiveRisk();
                });

                tag.appendChild(txt);
                tag.appendChild(btn);
                panel.appendChild(tag);
            });

            document.getElementById('symCount').textContent = tags.length;
        }

        function updateLiveRisk(){
            const ta = document.getElementById('symptoms');
            const tags = uniqueList(normalizeCommaList(ta.value));

            const moderate = [
                "high fever", "vomiting", "diarrhea", "severe headache", "dizziness"
            ];

            const hasModerate = tags.some(t => moderate.includes(t));

            if(hasModerate || tags.length >= 4){
                setRisk("warn", "Moderate", "Medium", "Symptoms look moderate. System may suggest guidance. If symptoms persist, consult a doctor.");
                return;
            }

            setRisk("ok", "Normal", "Low", "Symptoms look mild. System will predict using ML and show guidance if confidence is low.");
        }

        // Quick add chips functionality
        document.querySelectorAll('.chip').forEach(chip => {
            chip.addEventListener('click', () => {
                const s = chip.getAttribute('data-s');
                const ta = document.getElementById('symptoms');

                const current = uniqueList(normalizeCommaList(ta.value));
                if(!current.includes(s.toLowerCase())){
                    current.push(s.toLowerCase());
                }

                ta.value = setCommaList(current);
                renderTags();
                updateLiveRisk();
            });
        });

        const handleInput = debounce(() => {
            renderTags();
            updateLiveRisk();
        }, 300);

        document.getElementById('symptoms').addEventListener('input', handleInput);

        // Reset
        document.getElementById('resetBtn').addEventListener('click', () => {
            setTimeout(() => {
                renderTags(); // Will hit the 0 length condition and reset UI
                updateLiveRisk();
            }, 0);
        });

        // Form Validation
        document.getElementById('symptomForm').addEventListener('submit', (e) => {
            const tags = uniqueList(normalizeCommaList(document.getElementById('symptoms').value));
            const err = document.getElementById('symError');

            if(tags.length < 2){
                e.preventDefault();
                err.classList.remove('hidden');
                err.classList.add('block');
                document.getElementById('symptoms').classList.add('border-rose-500', 'focus:ring-rose-500');
                return;
            }

            err.classList.add('hidden');
            err.classList.remove('block');
            document.getElementById('symptoms').classList.remove('border-rose-500', 'focus:ring-rose-500');
        });

        // Initialize state on page load
        updateLiveRisk();
        renderTags();
    