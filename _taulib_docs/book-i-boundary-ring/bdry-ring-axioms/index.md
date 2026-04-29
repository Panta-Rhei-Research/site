---
{
  "projection_kind": "taulib_declaration",
  "title": "bdry_ring_axioms",
  "permalink": "/verify/taulib/docs/book-i-boundary-ring/bdry-ring-axioms/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Ring`.",
  "declaration_id": "TauLib.BookI.Boundary.Ring::bdry_ring_axioms",
  "declaration_slug": "bdry-ring-axioms",
  "kind": "theorem",
  "name": "bdry_ring_axioms",
  "module_name": "TauLib.BookI.Boundary.Ring",
  "module_url": "/verify/taulib/docs/book-i-boundary-ring/",
  "source_line_start": 270,
  "source_line_end": 292,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L270-L292",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L270-L292",
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
- Source path: [`TauLib/BookI/Boundary/Ring.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Ring.lean#L270-L292)
- Source range: L270-L292
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Full boundary ring axioms: all eight ring properties, proved universally. -/
```

## Source Excerpt

```lean
theorem bdry_ring_axioms :
    (∀ (n1 n2 d : TauIdx),
      (mk_omega_tail_add n1 n2 d).components = (mk_omega_tail_add n2 n1 d).components) ∧
    (∀ (n1 n2 n3 d : TauIdx),
      (mk_omega_tail_add (n1 + n2) n3 d).components =
      (mk_omega_tail_add n1 (n2 + n3) d).components) ∧
    (∀ (n d : TauIdx),
      (mk_omega_tail_add n 0 d).components = (mk_omega_tail n d).components) ∧
    (∀ (n d : TauIdx) (i : Nat), i < d →
      (mk_omega_tail_add n ((primorial d - n % primorial d) % primorial d) d).components.getD i 0 =
      (mk_omega_zero d).components.getD i 0) ∧
    (∀ (n1 n2 d : TauIdx),
      (mk_omega_tail_mul n1 n2 d).components = (mk_omega_tail_mul n2 n1 d).components) ∧
    (∀ (n1 n2 n3 d : TauIdx),
      (mk_omega_tail_mul (n1 * n2) n3 d).components =
      (mk_omega_tail_mul n1 (n2 * n3) d).components) ∧
    (∀ (n d : TauIdx),
      (mk_omega_tail_mul n 1 d).components = (mk_omega_tail n d).components) ∧
    (∀ (n1 n2 n3 d : TauIdx),
      (mk_omega_tail_mul n1 (n2 + n3) d).components =
      (mk_omega_tail_add (n1 * n2) (n1 * n3) d).components) :=
  ⟨omega_add_comm, omega_add_assoc, omega_add_zero, omega_add_neg_cancel,
   omega_mul_comm, omega_mul_assoc, omega_mul_one, omega_left_distrib⟩
```
