---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_add_neg_cancel",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/omega-add-neg-cancel/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::omega_add_neg_cancel",
  "declaration_slug": "omega-add-neg-cancel",
  "kind": "theorem",
  "name": "omega_add_neg_cancel",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/verify/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 245,
  "source_line_end": 263,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L245-L263",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L245-L263",
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
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L245-L263)
- Source range: L245-L263
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Additive inverse: n + neg(n) = 0 (on components). -/
```

## Source Excerpt

```lean
theorem omega_add_neg_cancel (n d : TauIdx) :
    ∀ (i : Nat), i < d →
    (mk_omega_tail_add n ((primorial d - n % primorial d) % primorial d) d).components.getD i 0 =
    (mk_omega_zero d).components.getD i 0 := by
  intro i hi
  have h_add := omega_add_components_eq n ((primorial d - n % primorial d) % primorial d) d
  rw [show (mk_omega_tail_add n ((primorial d - n % primorial d) % primorial d) d).components.getD i 0 =
    (mk_omega_tail (n + (primorial d - n % primorial d) % primorial d) d).components.getD i 0 from
    congrArg (fun l => l.getD i 0) h_add]
  rw [mk_omega_tail_getD _ d i hi]
  rw [show (mk_omega_zero d) = mk_omega_tail 0 d from rfl]
  rw [mk_omega_tail_getD 0 d i hi]
  unfold reduce
  rw [show (0 : Nat) % primorial (i + 1) = 0 from Nat.zero_mod _]
  have hidvd : primorial (i + 1) ∣ primorial d := primorial_dvd (show i + 1 ≤ d by omega)
  rw [Nat.add_mod n _ (primorial (i + 1))]
  rw [mod_mod_of_dvd _ _ _ hidvd]
  rw [neg_mod_dvd n hidvd]
  exact add_neg_cancel_mod n (primorial (i + 1)) (primorial_pos (i + 1))
```
