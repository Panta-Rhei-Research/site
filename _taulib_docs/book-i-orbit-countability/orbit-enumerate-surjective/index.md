---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_enumerate_surjective",
  "permalink": "/verify/taulib/docs/book-i-orbit-countability/orbit-enumerate-surjective/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Countability`.",
  "declaration_id": "TauLib.BookI.Orbit.Countability::orbit_enumerate_surjective",
  "declaration_slug": "orbit-enumerate-surjective",
  "kind": "theorem",
  "name": "orbit_enumerate_surjective",
  "module_name": "TauLib.BookI.Orbit.Countability",
  "module_url": "/verify/taulib/docs/book-i-orbit-countability/",
  "source_line_start": 38,
  "source_line_end": 43,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L38-L43",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Countability",
        "url": "/verify/taulib/docs/book-i-orbit-countability/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L38-L43",
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

- Module: [TauLib.BookI.Orbit.Countability](/verify/taulib/docs/book-i-orbit-countability/)
- Source path: [`TauLib/BookI/Orbit/Countability.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L38-L43)
- Source range: L38-L43
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.P04 part 2] Orbit enumeration hits every orbit ray element. -/
```

## Source Excerpt

```lean
theorem orbit_enumerate_surjective (g : Generator) (hg : g ≠ omega)
    (x : TauObj) (hx : OrbitRay g x) :
    ∃ n, orbitEnumerate g hg n = x := by
  obtain ⟨hseed, _⟩ := hx
  exact ⟨x.depth, by
    cases x; simp [orbitEnumerate] at hseed ⊢; exact hseed.symm⟩
```
