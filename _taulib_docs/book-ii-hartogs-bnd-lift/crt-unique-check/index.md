---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_unique_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/crt-unique-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::crt_unique_check",
  "declaration_slug": "crt-unique-check",
  "kind": "def",
  "name": "crt_unique_check",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 69,
  "source_line_end": 83,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L69-L83",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L69-L83",
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
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L69-L83)
- Source range: L69-L83
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT check: a and b uniquely determine x mod P_{n+1}.
    For all x in [0, P_{n+1}), the pair (x mod P_n, x mod p_{n+1})
    is unique. Verify by checking no collisions in range. -/
```

## Source Excerpt

```lean
def crt_unique_check (stage : TauIdx) : Bool :=
  let pn1 := primorial (stage + 1)
  if pn1 <= 1 then true
  else go 0 0 (pn1 * pn1)
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= primorial (stage + 1) then true
    else if y >= primorial (stage + 1) then go (x + 1) (x + 2) (fuel - 1)
    else if x == y then go x (y + 1) (fuel - 1)
    else
      let dx := crt_decompose x stage
      let dy := crt_decompose y stage
      (dx != dy) && go x (y + 1) (fuel - 1)
  termination_by fuel
```
