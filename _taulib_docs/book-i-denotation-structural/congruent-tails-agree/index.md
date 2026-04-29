---
{
  "projection_kind": "taulib_declaration",
  "title": "congruent_tails_agree",
  "permalink": "/verify/taulib/docs/book-i-denotation-structural/congruent-tails-agree/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.Structural`.",
  "declaration_id": "TauLib.BookI.Denotation.Structural::congruent_tails_agree",
  "declaration_slug": "congruent-tails-agree",
  "kind": "theorem",
  "name": "congruent_tails_agree",
  "module_name": "TauLib.BookI.Denotation.Structural",
  "module_url": "/verify/taulib/docs/book-i-denotation-structural/",
  "source_line_start": 303,
  "source_line_end": 312,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L303-L312",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Structural",
        "url": "/verify/taulib/docs/book-i-denotation-structural/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L303-L312",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Denotation.Structural](/verify/taulib/docs/book-i-denotation-structural/)
- Source path: [`TauLib/BookI/Denotation/Structural.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Structural.lean#L303-L312)
- Source range: L303-L312
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Finite stabilization**: two numbers congruent modulo M_k produce
    omega-tails that agree at level k.  This is the mechanism behind
    Cauchy-compactness: agreement at level k is determined by a finite check. -/
```

## Source Excerpt

```lean
theorem congruent_tails_agree (n m d k : TauIdx)
    (hk1 : 1 ≤ k) (hkd : k ≤ d)
    (hmod : n % primorial k = m % primorial k) :
    (mk_omega_tail n d).get (k - 1) = (mk_omega_tail m d).get (k - 1) := by
  simp only [OmegaTail.get]
  have hlt : k - 1 < d := by simp only [TauIdx] at *; omega
  rw [mk_omega_tail_getD n d (k - 1) hlt, mk_omega_tail_getD m d (k - 1) hlt]
  have hk : k - 1 + 1 = k := by simp only [TauIdx] at *; omega
  rw [hk]
  exact hmod
```
