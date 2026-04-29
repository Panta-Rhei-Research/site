---
{
  "projection_kind": "taulib_declaration",
  "title": "four_gen_ladder_incomplete",
  "permalink": "/verify/taulib/docs/book-i-orbit-too-few/four-gen-ladder-incomplete/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.TooFew`.",
  "declaration_id": "TauLib.BookI.Orbit.TooFew::four_gen_ladder_incomplete",
  "declaration_slug": "four-gen-ladder-incomplete",
  "kind": "theorem",
  "name": "four_gen_ladder_incomplete",
  "module_name": "TauLib.BookI.Orbit.TooFew",
  "module_url": "/verify/taulib/docs/book-i-orbit-too-few/",
  "source_line_start": 98,
  "source_line_end": 100,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L98-L100",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.TooFew",
        "url": "/verify/taulib/docs/book-i-orbit-too-few/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L98-L100",
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

- Module: [TauLib.BookI.Orbit.TooFew](/verify/taulib/docs/book-i-orbit-too-few/)
- Source path: [`TauLib/BookI/Orbit/TooFew.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooFew.lean#L98-L100)
- Source range: L98-L100
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.T09b] **Four-Generator Ladder Incompleteness**:
    With only 4 generators, the iterator ladder cannot be completed.
    The exponentiation level has no canonical orbit channel because
    only 2 solenoidal generators (π, γ) exist, but 3 rewiring levels
    (addition, multiplication, exponentiation) are needed.

    This shows that dropping a generator from 5 to 4 breaks
    ladder completeness — 5 generators is *necessary*. -/
```

## Source Excerpt

```lean
theorem four_gen_ladder_incomplete :
    ladder4Channel .exp_level = none ∧ solenoidal4.length < 3 :=
  ⟨rfl, by decide⟩
```
