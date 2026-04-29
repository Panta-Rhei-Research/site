---
{
  "projection_kind": "taulib_declaration",
  "title": "neg_mod_dvd",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/neg-mod-dvd/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::neg_mod_dvd",
  "declaration_slug": "neg-mod-dvd",
  "kind": "theorem",
  "name": "neg_mod_dvd",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/verify/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 102,
  "source_line_end": 114,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L102-L114",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Ring",
        "url": "/verify/taulib/docs/book-i-boundary-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L102-L114",
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

- Module: [TauLib.BookI.Boundary.Ring](/verify/taulib/docs/book-i-boundary-ring/)
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L102-L114)
- Source range: L102-L114
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Core identity: (M_d - n%M_d) % M_k = (M_k - n%M_k) % M_k when M_k | M_d.
    Proof: factor M_d = M_k * c, apply mul_sub_mod, then use mod_mod_of_dvd. -/
```

## Source Excerpt

```lean
private theorem neg_mod_dvd (n : Nat) {k d : Nat} (hdvd : primorial k ∣ primorial d) :
    (primorial d - n % primorial d) % primorial k =
    (primorial k - n % primorial k) % primorial k := by
  have hpos_k : primorial k > 0 := primorial_pos k
  have hpos_d : primorial d > 0 := primorial_pos d
  have hn_lt : n % primorial d < primorial d := Nat.mod_lt n hpos_d
  obtain ⟨c, hc⟩ := hdvd
  -- Rewrite LHS using M_d = M_k * c
  rw [show primorial d = primorial k * c from hc] at hn_lt ⊢
  -- Goal: (M_k*c - n%(M_k*c)) % M_k = (M_k - n%M_k) % M_k
  rw [mul_sub_mod (primorial k) hpos_k c _ (Nat.le_of_lt hn_lt)]
  -- Goal: (M_k - (n%(M_k*c)) % M_k) % M_k = (M_k - n%M_k) % M_k
  rw [mod_mod_of_dvd n (primorial k) (primorial k * c) ⟨c, rfl⟩]
```
