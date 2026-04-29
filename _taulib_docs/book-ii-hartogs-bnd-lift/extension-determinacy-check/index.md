---
{
  "projection_kind": "taulib_declaration",
  "title": "extension_determinacy_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/extension-determinacy-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::extension_determinacy_check",
  "declaration_slug": "extension-determinacy-check",
  "kind": "def",
  "name": "extension_determinacy_check",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 315,
  "source_line_end": 327,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L315-L327",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L315-L327",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookII.Hartogs.BndLift](/verify/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L315-L327)
- Source range: L315-L327
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The BndLift extension is determined by the CRT structure.
    For all x in [0, P_{n+1}), the lifted value equals x itself
    (since reduce(x, n+1) = x for x < P_{n+1}).
    This shows the lift is surjective onto the stage-(n+1) residues. -/
```

## Source Excerpt

```lean
def extension_determinacy_check (stage : TauIdx) : Bool :=
  let pn1 := primorial (stage + 1)
  if pn1 <= 1 then true
  else go 0 pn1
where
  go (x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= primorial (stage + 1) then true
    else
      -- For x < P_{n+1}: reduce(x, n+1) = x
      (bndlift x stage == x) &&
      go (x + 1) (fuel - 1)
  termination_by fuel
```
