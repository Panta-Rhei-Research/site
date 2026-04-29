---
{
  "projection_kind": "taulib_declaration",
  "title": "ontic_closure_five_way",
  "permalink": "/verify/taulib/docs/book-i-orbit-closure/ontic-closure-five-way/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Closure`.",
  "declaration_id": "TauLib.BookI.Orbit.Closure::ontic_closure_five_way",
  "declaration_slug": "ontic-closure-five-way",
  "kind": "theorem",
  "name": "ontic_closure_five_way",
  "module_name": "TauLib.BookI.Orbit.Closure",
  "module_url": "/verify/taulib/docs/book-i-orbit-closure/",
  "source_line_start": 46,
  "source_line_end": 55,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L46-L55",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Closure",
        "url": "/verify/taulib/docs/book-i-orbit-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L46-L55",
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

- Module: [TauLib.BookI.Orbit.Closure](/verify/taulib/docs/book-i-orbit-closure/)
- Source path: [`TauLib/BookI/Orbit/Closure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Closure.lean#L46-L55)
- Source range: L46-L55
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Ontic closure: five-way decomposition. -/
```

## Source Excerpt

```lean
theorem ontic_closure_five_way (x : TauObj) :
    OrbitRay alpha x ∨ OrbitRay pi x ∨
    OrbitRay gamma x ∨ OrbitRay eta x ∨
    x.seed = omega := by
  cases h : x.seed with
  | alpha => exact Or.inl ⟨h, by decide⟩
  | pi => exact Or.inr (Or.inl ⟨h, by decide⟩)
  | gamma => exact Or.inr (Or.inr (Or.inl ⟨h, by decide⟩))
  | eta => exact Or.inr (Or.inr (Or.inr (Or.inl ⟨h, by decide⟩)))
  | omega => exact Or.inr (Or.inr (Or.inr (Or.inr rfl)))
```
