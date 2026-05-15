---
{
  "projection_kind": "taulib_declaration",
  "title": "alpha_ray_member",
  "permalink": "/corpus/taulib/docs/book-ii-transcendentals-lines/alpha-ray-member/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.Lines`.",
  "declaration_id": "TauLib.BookII.Transcendentals.Lines::alpha_ray_member",
  "declaration_slug": "alpha-ray-member",
  "kind": "def",
  "name": "alpha_ray_member",
  "module_name": "TauLib.BookII.Transcendentals.Lines",
  "module_url": "/corpus/taulib/docs/book-ii-transcendentals-lines/",
  "source_line_start": 36,
  "source_line_end": 38,
  "registry_ids": [
    "II.D24"
  ],
  "related_registry_items": [
    {
      "id": "II.D24",
      "title": "Alpha-Ray Line",
      "url": "/registry/object/II.D24/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L36-L38",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.Lines",
        "url": "/corpus/taulib/docs/book-ii-transcendentals-lines/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L36-L38",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Transcendentals.Lines](/corpus/taulib/docs/book-ii-transcendentals-lines/)
- Source path: [`TauLib/BookII/Transcendentals/Lines.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/Lines.lean#L36-L38)
- Source range: L36-L38
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.D24` — Alpha-Ray Line

## Immediate Comment / Docstring

```lean
/-- [II.D24] Alpha-ray membership: x belongs to the alpha-ray with
    prime direction a iff its ABCD chart has A = a, B = 1, C = 1.
    The D-coordinate varies freely (subject to constraint C3). -/
```

## Source Excerpt

```lean
def alpha_ray_member (x a : TauIdx) : Bool :=
  let p := from_tau_idx x
  p.a == a && p.b == 1 && p.c == 1
```
