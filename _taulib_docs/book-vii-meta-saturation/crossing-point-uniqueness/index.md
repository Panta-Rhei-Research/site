---
{
  "projection_kind": "taulib_declaration",
  "title": "crossing_point_uniqueness",
  "permalink": "/corpus/taulib/docs/book-vii-meta-saturation/crossing-point-uniqueness/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Saturation`.",
  "declaration_id": "TauLib.BookVII.Meta.Saturation::crossing_point_uniqueness",
  "declaration_slug": "crossing-point-uniqueness",
  "kind": "theorem",
  "name": "crossing_point_uniqueness",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_url": "/corpus/taulib/docs/book-vii-meta-saturation/",
  "source_line_start": 228,
  "source_line_end": 236,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L228-L236",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Saturation",
        "url": "/corpus/taulib/docs/book-vii-meta-saturation/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L228-L236",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookVII.Meta.Saturation](/corpus/taulib/docs/book-vii-meta-saturation/)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean#L228-L236)
- Source range: L228-L236
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [VII.Lxx] Crossing Point Uniqueness: the lemniscate L = S¹ ∨ S¹ has
    exactly one crossing point p₀. This is the wedge point where the two
    lobes meet. No additional crossing points constructible. -/
```

## Source Excerpt

```lean
theorem crossing_point_uniqueness :
    -- π″ is the unique crossing mediator
    Generator.pi_dprime.orbit = .crossing ∧
    -- No other generator maps to crossing orbit
    Generator.alpha.orbit ≠ .crossing ∧
    Generator.pi.orbit ≠ .crossing ∧
    Generator.pi_prime.orbit ≠ .crossing ∧
    Generator.omega.orbit ≠ .crossing :=
  ⟨rfl, by decide, by decide, by decide, by decide⟩
```
