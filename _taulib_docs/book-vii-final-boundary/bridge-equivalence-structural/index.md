---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_equivalence_structural",
  "permalink": "/verify/taulib/docs/book-vii-final-boundary/bridge-equivalence-structural/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Final.Boundary`.",
  "declaration_id": "TauLib.BookVII.Final.Boundary::bridge_equivalence_structural",
  "declaration_slug": "bridge-equivalence-structural",
  "kind": "theorem",
  "name": "bridge_equivalence_structural",
  "module_name": "TauLib.BookVII.Final.Boundary",
  "module_url": "/verify/taulib/docs/book-vii-final-boundary/",
  "source_line_start": 83,
  "source_line_end": 87,
  "registry_ids": [
    "VII.T46"
  ],
  "related_registry_items": [
    {
      "id": "VII.T46",
      "title": "Bridge Equivalence at S_L",
      "url": "/registry/object/VII.T46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L83-L87",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Final.Boundary",
        "url": "/verify/taulib/docs/book-vii-final-boundary/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L83-L87",
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

- Module: [TauLib.BookVII.Final.Boundary](/verify/taulib/docs/book-vii-final-boundary/)
- Source path: [`TauLib/BookVII/Final/Boundary.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Final/Boundary.lean#L83-L87)
- Source range: L83-L87
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T46` — Bridge Equivalence at S_L

## Immediate Comment / Docstring

```lean
/-- [VII.T46] Bridge Equivalence at S_L (ch120). The structural parts:
    B_{D→C} restricted to S_L satisfies faithfulness, fullness, and
    essential surjectivity. These are the diagrammatic components.

    **sorry**: methodological boundary — the equivalence statement involves
    ω-content (the bridge succeeds precisely because D-C coincide at S_L,
    which involves ω as crossing mediator). The structural fields are
    verified; the categorical equivalence claim transcends Reg_D. -/
```

## Source Excerpt

```lean
theorem bridge_equivalence_structural :
    bridge_functor.faithful_at_sl = true ∧
    bridge_functor.full_at_sl = true ∧
    bridge_functor.ess_surj_at_sl = true :=
  ⟨rfl, rfl, rfl⟩
```
